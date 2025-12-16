import pandas as pd
import time

Slots = 2
File = "contatos.csv"

Message = "da vaga para o treinamento Domínio SIEM é:"
Message_end = "Ele/ela está na live?"

VERDE = "\033[1;32m"
RESET = "\033[0m"
AMARELO = "\033[1;33m"
VERMELHO = "\033[1;31m"

def mascarar_email(email: str) -> str:
    usuario, dominio = email.split('@', 1)

    if len(usuario) > 4:
        usuario_mascarado = usuario[:-4] + '****'
    elif len(usuario) > 2:
        usuario_mascarado = usuario[:-2] + '**'
    else:
        usuario_mascarado = '**'

    return f"{usuario_mascarado}@{dominio}"

def pergunta_esta_na_live() -> bool:
    while True:
        resp = input(f"{AMARELO}{Message_end} (s/n): {RESET}").strip().lower()
        if resp in ("s", "sim", "y", "yes"):
            return True
        if resp in ("n", "nao", "não", "no"):
            return False
        print(f"{VERMELHO}Resposta inválida. Digite 's' ou 'n'.{RESET}")

def load_():
    x = 0
    while x < 10:
        print(".")
        x = x + 1
        time.sleep(0.4)
    return 0

df = pd.read_csv(File, delimiter=';')

df['Email'] = df['Email'].astype(str).str.strip()
df = df[df['Email'].str.contains('@', na=False)]

Start = 1
while Start <= Slots:
    if df.empty:
        print(f"{VERMELHO}Acabaram os e-mails para sortear.{RESET}")
        break

    sorteado = df.sample(n=1)
    idx = sorteado.index[0]
    email_sorteado = sorteado['Email'].values[0]
    email_mascarado = mascarar_email(email_sorteado)

    print(f"{VERDE}~ ### O {Start}ª ganhador {Message}{RESET}")
    load_()
    time.sleep(1)
    print(f"{VERDE}{email_mascarado}{RESET}")

    if pergunta_esta_na_live():
        print(f"{VERDE}✅ Confirmado!{RESET}\n")
        df = df.drop(index=idx)
        Start += 1
        time.sleep(2)
    else:
        print(f"{VERMELHO}❌ Sorteando outro...{RESET}\n")
        df = df.drop(index=idx)
        time.sleep(2)
