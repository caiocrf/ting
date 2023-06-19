from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    data = txt_importer(path_file)

    list_data = [
        instance.search(i)["nome_do_arquivo"] for i in range(len(instance))
    ]

    if path_file not in list_data:
        list_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }

        instance.enqueue(list_data)
        sys.stdout.write(str(list_data))


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        file_data = instance.dequeue()
        file_path = file_data["nome_do_arquivo"]
        print(f"Arquivo {file_path} removido com sucesso")


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        print(metadata)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
