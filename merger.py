import glob

file_list = glob.glob('scripts/*/*.txt')


with open('All_merged.txt' , 'w') as output_file:
    for file in file_list:
        with open(file) as input_file:
            print(f'Merging {file}...')
            contents = input_file.read()
            output_file.write(contents)

print("Complete!")