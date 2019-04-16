import os
from PIL import Image
from shutil import copyfile

def repaint_file(in_path, out_path):
  out_dir_path = os.path.dirname(out_path)
  if not os.path.isdir(out_dir_path):
    os.mkdir(out_dir_path)

  im = Image.open(in_path)
  if im.format == 'GIF':
    # im.save(out_path + '.gif', format='webp', save_all=True)
    copyfile(in_path, out_path + '.gif')
  else:
    im.save(out_path + '.jpg', format='webp', quality=75)
  im.close()

def create_out_path(out_dir_path, relative_path, file_name):
  portion = os.path.splitext(file_name)
  file_name = portion[0]
  return os.path.join(out_dir_path, relative_path, file_name)

def repaint_dir(in_dir_path, out_dir_path):
  if not os.path.isdir(out_dir_path):
    os.mkdir(out_dir_path)
  for path, dir_list, file_list in os.walk(in_dir_path):
    relative_path = path.lstrip(in_dir_path + os.sep)
    for file_name in file_list:  
        file_path = os.path.join(path, file_name)
        file_out_path = create_out_path(out_dir_path, relative_path, file_name)
        repaint_file(file_path, file_out_path)
        print('转换 {} => {}'.format(file_path, file_out_path))

def main():
  repaint_dir('./test/原始', './test/输出')

  # repaint_file('./test/原始/501.jpg', './test/输出/501.jpg')


if __name__ == '__main__':
  main()
