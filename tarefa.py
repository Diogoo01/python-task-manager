from utils import data_atual
from datetime import datetime


class Tarefa:
    def __init__(
        self,
        nome,
        descricao,
        categoria,
        prioridade,
        prazo=None,
        concluida=False,
        criada_em=None,
    ):
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.prioridade = prioridade
        self.concluida = concluida
        self.criada_em = criada_em if criada_em is not None else data_atual()
        self.prazo = prazo

    def para_dict(self):
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "prioridade": self.prioridade,
            "concluida": self.concluida,
            "criada_em": self.criada_em,
            "prazo": self.prazo,
        }

    @classmethod
    def de_dict(cls, dados):
        return cls(
            nome=dados["nome"],
            descricao=dados["descricao"],
            categoria=dados["categoria"],
            prioridade=dados["prioridade"],
            prazo=dados["prazo"],
            concluida=dados["concluida"],
            criada_em=dados["criada_em"],
        )

    def concluir(self):
        self.concluida = True

    def esta_atrasada(self):
        if self.prazo is None:
            return False

        if self.concluida:
            return False

        prazo_data = datetime.strptime(
            self.prazo,
            "%Y-%m-%d %H:%M:%S",
        )

        return prazo_data < datetime.now()

    def estado_prazo(self):
        if self.prazo is None:
            return "Sem prazo"

        prazo_data = datetime.strptime(
            self.prazo,
            "%Y-%m-%d %H:%M:%S",
        )

        agora = datetime.now()

        if self.concluida:
            return "Concluída"

        if self.esta_atrasada():
            return "Atrasada"

        diferenca = prazo_data - agora
        segundos = int(diferenca.total_seconds())

        dias = segundos // 86400
        horas = segundos // 3600
        minutos = segundos // 60

        anos = dias // 365
        if anos >= 1:
            return "Falta 1 ano" if anos == 1 else f"Faltam {anos} anos"

        meses = dias // 30
        if meses >= 1:
            return "Falta 1 mês" if meses == 1 else f"Faltam {meses} meses"

        if dias >= 1:
            return "Falta 1 dia" if dias == 1 else f"Faltam {dias} dias"

        if horas >= 1:
            return "Falta 1 hora" if horas == 1 else f"Faltam {horas} horas"

        if minutos >= 1:
            return "Falta 1 minuto" if minutos == 1 else f"Faltam {minutos} minutos"

        return "Falta 1 segundo" if segundos == 1 else f"Faltam {segundos} segundos"
