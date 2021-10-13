import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""

    instance.enqueue(path_file)
    sys.stdout.write(f"'nome_do_arquivo': '{path_file}'\n"),
    sys.stdout.write(f"'qtd_linhas': {len(txt_importer(path_file))}\n"),
    sys.stdout.write(f"'linhas_do_arquivo': {txt_importer(path_file)}\n"),


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) != 0:
        removed = instance.dequeue()
        sys.stdout.write(f"Arquivo {removed} removido com sucesso\n")
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        answer = instance.search(position)
        sys.stdout.write(answer)
    except IndexError:
        sys.stderr.write("Posição inválida")
