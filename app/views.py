from winreg import DeleteKey
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Funcionario



class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = '__all__'  # Incluir todos os campos do modelo Funcionario
    template_name = 'app/form_funcionario.html'  # Caminho correto para o template
    success_url = '/app/lista_funcionarios'  # URL para redirecionar após o sucesso

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'app/lista_funcionarios.html'  # O template a ser usado
    context_object_name = 'funcionarios'  # Nome da variável que será usada no template

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = '__all__'  # Permite editar todos os campos do modelo Funcionario
    template_name = 'app/form_funcionario.html'  # Reutiliza o template de cadastro
    success_url = reverse_lazy('lista_funcionarios')  # Redireciona para a lista de funcionários após a atualização

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'app/lista_funcionario.html'  # Template para exibir os dados do funcionário
    context_object_name = 'fun'  # Nome da variável no template para acessar o funcionário

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'app/remover_funcionario.html'
    success_url = reverse_lazy('lista_funcionarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fun'] = self.object  # Passa o objeto do funcionário para o template
        return context