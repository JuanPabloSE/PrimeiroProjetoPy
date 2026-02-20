def calcular_media(nota1, nota2):

    return (nota1 + nota2) / 2

def validar_quantidade_alunos():

    while True:
        try:
            quantidade = int(input("\nQual a quantidade de alunos? (Entre 2 e 7 alunos): "))
            if 2 <= quantidade <= 7:
                return quantidade
            else:
                print("❌ Erro: A quantidade deve estar entre 2 e 7 alunos!")
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido!")

def validar_nota():

    while True:
        try:
            nota = float(input("Digite a nota (0,0 - 10,0): "))
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print("❌ Erro: A nota deve estar entre 0,0 e 10,0!")
        except ValueError:
            print("❌ Erro: Digite um número válido!")


def coletar_dados_alunos(quantidade):

    alunos = []

    for i in range(1, quantidade + 1):
        print(f"\n{'='*50}")
        print(f"Aluno {i} de {quantidade}")
        print(f"{'='*50}")

        nome = input("Digite o nome do aluno: ").strip()
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            i -= 1
            continue

        print("\nDigite as duas notas do aluno:")
        nota1 = validar_nota()
        nota2 = validar_nota()

        media = calcular_media(nota1, nota2)

        aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media
        }

        alunos.append(aluno)

    return alunos


def exibir_resultados(alunos):

    print(f"\n\n{'='*70}")
    print(f"{'RESULTADO FINAL':^70}")
    print(f"{'='*70}")
    print(f"{'Nome do Aluno':<25} {'Nota 1':<12} {'Nota 2':<12} {'Média':<10}")
    print(f"{'-'*70}")

    for aluno in alunos:
        print(f"{aluno['nome']:<25} {aluno['nota1']:<12.2f} {aluno['nota2']:<12.2f} {aluno['media']:<10.2f}")

    print(f"{'='*70}\n")

    print(f"Quantidade de alunos na turma: {len(alunos)}")
    media_geral = sum(aluno['media'] for aluno in alunos) / len(alunos)
    print(f"Média geral da turma: {media_geral:.2f}")

    melhor_aluno = max(alunos, key=lambda x: x['media'])
    print(f"Melhor desempenho: {melhor_aluno['nome']} com média {melhor_aluno['media']:.2f}")

    pior_aluno = min(alunos, key=lambda x: x['media'])
    print(f"Menor desempenho: {pior_aluno['nome']} com média {pior_aluno['media']:.2f}")


def main():

    print("\n" + "="*50)
    print("SISTEMA DE CÁLCULO DE MÉDIAS ESCOLARES")
    print("="*50)

    quantidade = validar_quantidade_alunos()

    alunos = coletar_dados_alunos(quantidade)

    exibir_resultados(alunos)


if __name__ == "__main__":
    main()
