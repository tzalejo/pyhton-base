
def run():
    with open('numero.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))


if __name__ == '__main__':
    run()

