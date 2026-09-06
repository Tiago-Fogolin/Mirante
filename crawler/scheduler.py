import sys
import os
import time
from datetime import date, timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crawler.main import main as rodar_crawlers

INTERVALO_SEGUNDOS = 2 * 60 * 60  # 2 horas


def loop():
    while True:
        hoje = date.today()
        ontem = hoje - timedelta(days=1)
        data_inicio = ontem.strftime("%d-%m-%Y")
        data_fim = hoje.strftime("%d-%m-%Y")

        try:
            rodar_crawlers(data_inicio, data_fim)
        except Exception as e:
            print(f"ERRO no ciclo do scheduler: {e}")

        print(f"Aguardando {INTERVALO_SEGUNDOS // 60} minutos até o próximo ciclo...")
        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    loop()
