class MinhaClasse:

    def __enter__(self):
        print("Entrei aqui!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou no exit.")


# contesto
# -> isso fica no meio da classe, no contexto da conexão da classe
with MinhaClasse() as mc:
    print("Entrei no With")

# output:
# Entrei aqui!
# Entrei no With
# Estou no exit.
