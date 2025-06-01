import smtplib
import time
import sqlite3

# Configurações do servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'gabeponte20@gmail.com'
SMTP_PASSWORD = 'hqypjbzuwxjbgbzu'


def send_email(from_addr, to_addr, subject, message):
    # Configurar conexão SMTP
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Montar o email
    email_message = f"From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{message}"

    # Enviar o email
    server.sendmail(from_addr, to_addr, email_message)

    # Encerrar a conexão SMTP
    server.quit()


def main():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()

    # Buscar os emails do banco de dados
    c.execute("SELECT email FROM emails")
    emails = c.fetchall()

    # Enviar emails
    from_addr = SMTP_USERNAME
    subject = 'Assunto do email'
    message = 'Corpo do email'

    for email in emails:
        to_addr = email[0]

        send_email(from_addr, to_addr, subject, message)

        print(f"Email enviado para: {to_addr}")

        # Aguardar 15 segundos entre cada envio de email
        time.sleep(1.2)

    conn.close()


if __name__ == '__main__':
    main()
