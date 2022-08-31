import argparse as ap
import sys
import os.path

# cd Documents\GitHub\N-model
# считываем передаваемые аргументы из командной строки и переносим их в нашу программу
# parser = ap.ArgumentParser()
# parser.add_argument('--input_dir', type=str, default='stdin')
# parser.add_argument('--model', type=str)
# args = parser.parse_args()
#
# file_to_save_model = args.model
#
# if args.input_dir != 'stdin':
#     dir_with_texts = args.input_dir
# else:
#     text_for_train = [i.rstrip('\n') for i in sys.stdin.readlines()]
#
#
# for i in range(count_of_docs):
#     with open(r'C:\Users\Пользователь\PycharmProjects\pythonProject\test.txt', 'r') as f:
#         data = f.read()
print(len([name for name in os.listdir(r'C:\Users\Пользователь\Desktop\data')]))