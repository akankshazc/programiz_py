# Python program to merge mails

with open('6_files/names.txt', 'r', encoding='utf-8') as f:

    with open('6_files/body.txt', 'r', encoding='utf-8') as b:

        body = b.read()

        for name in f:
            mail = "Hello " + name.strip() + "\n" + body

            with open(f'6_files/emails/{name.strip()}.txt', 'w', encoding='utf-8') as e:
                e.write(body)
                print(f'{name.strip()} done...')
