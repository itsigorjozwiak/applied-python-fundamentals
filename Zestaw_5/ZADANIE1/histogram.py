import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    from ZADANIE1.tablica import MonitorowanaTablica
except ModuleNotFoundError:
    from tablica import MonitorowanaTablica


def plot_histogram(tablica: MonitorowanaTablica, algo_name: str, fps=60):
    '''Rysuje proces sortowania.
    
    Argumenty:
    tablica (MonitorowanaTablica): tablica do posortowania
    algo_name (str): nazwa algorytmu
    fps (int): liczba klatek na sekunde w animiacj 
    '''
    plt.rcParams['font.size'] = 16
    fig, ax = plt.subplots(figsize=(16, 8))
    container = ax.bar(range(len(tablica)), tablica.pelne_kopie[0], align='edge', width=0.8)
    fig.suptitle(f'Sorting: {algo_name}')
    ax.set(xlabel='Index', ylabel='Value')
    ax.set_xlim([0, len(tablica)])
    txt = ax.text(0.01, 0.99, '', ha='left', va='top', transform=ax.transAxes)

    def update(frame: int):
        '''Aktualizacja histogramu po kazdym kroku sortowania.
        
        Argumenty:
        frame (int): Aktualnyu indeks klatki.
        '''
        txt.set_text(f'Operations = {frame}')
        for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
            rectangle.set_height(height)
            rectangle.set_color('darkblue')

        idx, op = tablica.aktywnosc(frame)
        if op == 'get':
            container.patches[idx].set_color('green')
        elif op == 'set':
            container.patches[idx].set_color('red')

        return (txt, *container)

    ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./fps, repeat=False)
    plt.show()
