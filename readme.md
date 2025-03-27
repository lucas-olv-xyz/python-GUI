# 🎨 Tkinter Web Launcher

Este projeto é uma aplicação gráfica simples desenvolvida com Tkinter. A interface apresenta uma janela com uma imagem, um rótulo e um botão. Ao clicar no botão, o usuário é redirecionado para um vídeo no YouTube através do navegador padrão.

---

## 🚀 Funcionalidades

- **Interface gráfica** criada com Tkinter.
- **Exibição de imagem**: Carrega e exibe a imagem `dream.gif`.
- **Rótulo personalizado**: Mostra um texto customizado (atualmente com placeholders).
- **Botão interativo**: Ao ser clicado, abre um link específico do YouTube no navegador padrão do usuário.

---

## 🛠️ Bibliotecas Utilizadas

- **tkinter**: Biblioteca padrão do Python para criação de interfaces gráficas.
- **webbrowser**: Biblioteca padrão para abrir URLs no navegador padrão.

---

## ▶️ Como Executar

1. **Certifique-se** de ter o Python instalado (versão 3.x).
2. **Verifique** se a imagem `dream.gif` está no mesmo diretório que o script.
3. **Execute o script** com o seguinte comando:
   ```bash
   python nome_do_arquivo.py
   ```
4. A janela da aplicação será aberta. Clique no botão para abrir o vídeo no YouTube.

---

## ⚙️ Personalização

- **Título e Rótulo**: Atualmente os textos estão definidos com placeholders (caracteres de interrogação). Edite as strings no código para personalizar o título da janela e o texto do rótulo.

  Exemplo:

  ```python
  window.title("Meu Projeto Tkinter")
  label = tk.Label(window, text="Bem-vindo ao Meu Projeto", bg='black')
  button = tk.Button(window, text="Abrir Vídeo", command=open_url)
  ```

- **URL**: Para alterar o vídeo ou página aberta, modifique a URL na função `open_url()`.

---

## 🧪 Código Completo

```python
import tkinter as tk
import webbrowser

# Cria a janela principal
window = tk.Tk()
window.title("????????????????????????????????????")  # Altere o título conforme desejado
window.geometry("900x600")
window.configure(bg='black')

def open_url():
    # Abre a URL no navegador padrão
    webbrowser.open("https://www.youtube.com/watch?v=OzBPyATdG-c&list=PLnh-TZzbBdaAMOm7sexgpBr01u3uFnjmA&index=4")

# Cria um rótulo e um botão
label = tk.Label(window, text="???????????????", bg='black')
label.configure(fg='red', font=('Inter', 20))

button = tk.Button(window, text="????????????", command=open_url)
button.configure(fg='pink', bg='black', font=('Inter', 12))
button.pack(side='bottom')

# Carrega a imagem
image = tk.PhotoImage(file='dream.gif')

label.pack(side='top', fill='both', expand=True)
label.configure(image=image)

# Organiza os widgets
label.pack()
button.pack()

# Inicia o loop principal da aplicação
window.mainloop()
```

---

## ⚠️ Observações

- **Placeholders**: Os textos com "??????????????" devem ser substituídos pelo conteúdo desejado.
- **Imagem**: Certifique-se de que o arquivo `dream.gif` existe no diretório para evitar erros ao carregar a imagem.
- **Dependências**: Tkinter e webbrowser fazem parte da biblioteca padrão do Python; não é necessário instalar pacotes adicionais.

---

## 📄 Licença

Este projeto é livre para uso e aprendizado. Sinta-se à vontade para modificar e aprimorar conforme suas necessidades.
