def exists_word(word, instance):
    search_result = list()
    for i in range(len(instance)):
        file = instance.search(i)
        occurrence = []

        for j, line in enumerate(file["linhas_do_arquivo"], 1):
           if word.lower() in line.lower():
            occurrence.append({"linha": j})

        if occurrence:
           result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": occurrence
           }
           search_result.append(result)

    return search_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
