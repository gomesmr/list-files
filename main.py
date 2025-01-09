import os

def gather_files(source_directory, file_type, output_file, exclude_dirs, file_name=None):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(source_directory):
            # Exclui diretórios que estejam na lista de exclusão
            dirs[:] = [d for d in dirs if all(excl.lower() not in d.lower() for excl in exclude_dirs)]
            for file in files:
                # Verifica se o arquivo corresponde ao nome e tipo especificados
                if file.endswith(f'.{file_type}') and (file_name is None or file_name in file):
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


if __name__ == '__main__':
    source_directory = ''
    output_file = ''
    file_type = 'java'

    # Array de diretórios a serem excluídos
    exclude_dirs = ['test', 'target']

    # Nome do arquivo ou parte dele a ser filtrado
    file_name = ''

    gather_files(source_directory, file_type, output_file, exclude_dirs, file_name)

    print(f'Conteúdo dos arquivos .{file_type} contendo "{file_name}" foi copiado para {output_file}')
