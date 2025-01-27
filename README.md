# projeto-final-pos-2024

É uma api que reúne filmes, acessorios, músicas etc da Barbie.  

## Instalação do Serviço 🛠️
Segue o passo a passo:

- Crie um ambiente virtual python 
```bash
python -m venv venv
```

- Ative o ambiente virtual

*powershell*
```powershell
.venv/Scripts/activate
```

*bash*
```bash
source venv/Scripts/activate
```

- Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

- Realize as migrações
```bash
python manage.py migrate
```

- Teste o serviço localmente, após rodar o comando a seguir
```powershel
python manage.py runserver
```

## Configurando o Cliente 🖥️
Com o serviço rodando, inicie outro terminal como, por exemplo, o *bash*

- No terminal, entre na pasta `📂 client_api/`
```bash
cd client_api/
```

- Após acessar a pasta `📂 client_api/`, instale as dependências necessárias do projeto utilizando o seguinte comando, que deve baixar o `node_modules`
```bash
npm install
```
- Por fim, execute o cliente localmente
```bash
npm run dev
```






