def run():
    with open('aleph.txt') as f:
        #print(f.readlines())
        counter = 0
        for line in f:
            counter += line.count('Beatriz')

        print('Beatriz se encuentra {} veces en el texto'.format(counter))

if __name__== '__main__':
    run()
