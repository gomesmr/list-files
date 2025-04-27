import os


def gather_files(source_directory, file_types, exclude_dirs, exclude_files=None, file_name=None):
    # Define o nome do arquivo de saída com base no último diretório do caminho
    output_file_name = f"{os.path.basename(source_directory)}.log"
    output_file_path = os.path.join(source_directory, output_file_name)

    # Garante que file_types seja uma lista
    if isinstance(file_types, str):
        file_types = [file_types]

    # Se file_types estiver vazio, inclui todos os tipos de arquivo
    include_all_files = not bool(file_types)

    # Garante que exclude_files seja uma lista, mesmo que None seja passado
    exclude_files = exclude_files or []

    # Adiciona o arquivo de saída à lista de exclusão
    exclude_files.append(output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(source_directory):
            # Exclui diretórios que estejam na lista de exclusão
            dirs[:] = [d for d in dirs if all(excl.lower() not in d.lower() for excl in exclude_dirs)]
            for file in files:
                # Verifica se o arquivo deve ser incluído (todos ou apenas os tipos especificados)
                file_matches_type = (include_all_files or
                                     any(file.endswith(f'.{ft}') for ft in file_types))
                # Verifica os outros critérios
                if (file_matches_type and
                        (file_name is None or file_name in file) and
                        file not in exclude_files):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(f"\nArquivo: {file_path}\n\n")
                            outfile.write(infile.read())
                            outfile.write("\n")
                    except FileNotFoundError:
                        print(f"Erro ao abrir o arquivo: {file_path}. Arquivo não encontrado")
                    except Exception as e:
                        print(f"Erro ao processar o arquivo: {file_path}. Detalhes do erro: {e}")

    # Mensagem de conclusão adaptada para ambos os casos
    if include_all_files:
        print(f'Conteúdo de todos os arquivos contendo "{file_name}" foi copiado para {output_file_path}')
    else:
        print(f'Conteúdo dos arquivos {file_types} contendo "{file_name}" foi copiado para {output_file_path}')


if __name__ == '__main__':
    source_directory = r'C:\Users\gomes\PhpstormProjects\news_matter'
    file_types = []  # Lista vazia incluirá todos os tipos de arquivo

    # Array de diretórios a serem excluídos
    exclude_dirs = ['.git', '.idea']

    # Lista de arquivos a serem excluídos
    exclude_files = ['.gitlab-ci.yml', 'NewsMatter.md', 'README.md', 'newsMatter.excalidraw', '.gitignore']

    # Incluir apenas arquivos que tenham o padrão abaixo
    file_name = ''

    gather_files(source_directory, file_types, exclude_dirs, exclude_files, file_name)