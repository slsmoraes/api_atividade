from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=29)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    #print(pessoa.nome, pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 27
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.delete()

def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    print(usuario)
    usuario.save()

def consulta_todos_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)
    #pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    #print(pessoa.nome, pessoa.idade)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #consulta_pessoa()
    #exclui_pessoa()
    #consulta_pessoa()
    insere_usuarios('Felipe', '123')
    consulta_todos_usuario()