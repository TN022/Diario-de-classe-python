class Aluno:
    def __init__(self, nome, nota1 , nota2, presenca, media, situacao):
        self.nome = nome
        self.presenca = presenca
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = media
        self.situacao = situacao


    @classmethod
    def criar_aluno(cls):
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota da P1 do aluno: "))
        nota2 = float(input("Digite a nota da P2 do aluno: "))
        faltas = float(input("Digite quantas aulas esse aluno faltou: "))
        total_de_aulas = float(input("Digite quantas aulas teve nesse semestre: "))
        presenca = ((total_de_aulas - faltas)/total_de_aulas)
        media = (nota1 + nota2) / 2
        if media >=7 and presenca >=75:
            situacao = 'Aprovado'
        elif media<7 and presenca >=75:
            situacao = 'Em recuperação'
        else:
            situacao = 'Reprovado'
        return cls(nome, nota1, nota2, presenca, media, situacao)
    
    
def mostrar_alunos():
    for aluno in alunos:
        print(f"===============================\nAluno : {aluno.nome}\nFrequência de aulas: {aluno.presenca:.1%}\nNota da P1: {aluno.nota1}\nNota da P2: {aluno.nota2}\nMédia: {aluno.media}\nO Aluno {aluno.nome} está: {aluno.situacao}!\n===============================")   

alunos = []

while True:
    aluno = Aluno.criar_aluno()
    alunos.append(aluno)

    continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().lower()
    if continuar != 's' and continuar != 'sim':
        break

mostrar_alunos()
