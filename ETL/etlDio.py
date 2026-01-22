import pandas as pd
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'itens.csv')
save_folder = os.path.join(dirname,'Total_Itens.csv')

df = pd.read_csv(filename, sep=';')
df['Valor_Total_Item'] = df['Valor'] * df['Quantidade']
resultado = df.groupby('Tipo').agg({
    'Quantidade': 'sum',
    'Valor_Total_Item': 'sum'
}).reset_index()
resultado = resultado.rename(columns={'Tipo':'Tipos de produto','Quantidade': 'Quantidade Total','Valor_Total_Item': 'Valor Total'})
resultado.to_csv(save_folder, sep=';', index=False)