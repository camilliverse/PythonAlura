equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

tarefas_combinadas = equipe_a.union(equipe_b)

tarefa_remover = input('Quais tarefas voce deseja remover: ').lower()

if tarefa_remover in tarefas_combinadas:
    tarefas_combinadas.remove(tarefa_remover)

print(f'Tareas finais: {tarefas_combinadas} ')