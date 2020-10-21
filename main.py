#### Step 1: Download
#### Step 2: Make sure the file you want to download has shared link that anyone can access
#### Step 3: Run
#### Step 4: Enjoy
####
print('1. Uploaded File')
print('2. Google Docs')
print('3. Google Slides')
print('4. Google Sheets')
in1 = input('Choose(1-4): ')

while in1 == '1':
    bob = input('Shared link: ')
    jane = bob[32:65]
    print('https://drive.google.com/uc?export=download&id=' + jane)
    break

while in1 == '2':
    print('Download As')
    print('1. .docx')
    print('2. .pdf')
    print('3. .txt')
    print('4. .html')
    in2 = input('Choose(1-4): ')

    while in2 == '1':
        idk111 = input('Shared link: ')
        sjnjf1 = idk111[0:79]
        print(sjnjf1 + '/export?format=doc')
        break

    while in2 == '2':
        idk111 = input('Shared link: ')
        sjnjf1 = idk111[0:79]
        print(sjnjf1 + '/export?format=pdf')
        break

    while in2 == '3':
        idk111 = input('Shared link: ')
        sjnjf1 = idk111[0:79]
        print(sjnjf1 + '/export?format=txt')
        break

    while in2 == '4':
        idk11123 = input('Shared link: ')
        sjnjf1 = idk11123[0:79]
        print(sjnjf1 + '/export?format=html')
        break
    break

while in1 == '3':
    print('Download As')
    print('1. .pptx')
    print('2. .pdf')
    in2 = input('Choose(1-2): ')
    
    while in2 == '1':
        tomandjerry = input('Shared Link: ')
        jerryandtom = tomandjerry[0:83]
        print(jerryandtom + '/export/pptx')
        break

    while in2 == '1':
        tomandjerry = input('Shared Link: ')
        jerryandtom = tomandjerry[0:83]
        print(jerryandtom + '/export/pdf')
        break
    break

while in1 == '4':
    print('Download As')
    print('1. .xlsx')
    print('2. .pdf')
    in2 = input('Choose(1-2): ')

    while in2 == '1':
        spongebob = input('Shared Link: ')
        patrick = spongebob[0:83]
        print(patrick + '/export?format=xlsx')
        break
    

    while in2 == '2':
        spongebob = input('Shared Link: ')
        patrick = spongebob[0:83]
        print(patrick + '/export?format=pdf')
        break
    break


    

    
















