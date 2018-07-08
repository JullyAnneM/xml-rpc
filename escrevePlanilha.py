import xlsxwriter 


def main():
    workbook = xlsxwriter.Workbook('dados_gRPC.xlsx')
    worksheet = workbook.add_worksheet()

    arq = open('tempos_gRPC.txt',  'r')
    texto = arq.readlines()
    inicializaWorksheet(texto, worksheet)
    row = 0
    col = 0
    
    for linha in texto :
        if(row%21 == 0):
            row = 0
            col = col + 1
        worksheet.write(row, col, linha.split(' ')[1].replace("\n", "").replace(".", ","))
        row += 1
    
    arq.close()

def inicializaWorksheet(texto, worksheet):
    col = 0
    row = 0
    for linha in texto:
        worksheet.write(row, col, linha.split(' ')[0])
        row += 1
        if(row == 21):
            break

if __name__ == "__main__":
    main()
 