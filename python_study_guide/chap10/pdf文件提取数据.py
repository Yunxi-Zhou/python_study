import pdfplumber
# 打开pdf
with pdfplumber.open('血液补偿协议.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())  # extract_text()提取内容

        print(f'-------------{i.page_number}end')
