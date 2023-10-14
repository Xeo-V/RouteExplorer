import osmnx as ox
import matplotlib.pyplot as plt
import tkinter as tk
import heapq

global click_count, orig, dest, graph, ax, path_found
click_count = 0
orig = None
dest = None
path_found = False

def fetch_and_plot_graph_by_bbox(north, south, east, west):
    return ox.graph_from_bbox(north, south, east, west, network_type='drive')

def heuristic(u, v):
    return graph.nodes[v]['y'] - graph.nodes[u]['y'] + graph.nodes[v]['x'] - graph.nodes[u]['x']

def astar_path(G, start, goal):
    open_list = [(0, start, [])]
    closed_list = set()
    explored_edges = set()
    min_x = max_x = G.nodes[start]['x']
    min_y = max_y = G.nodes[start]['y']
    while open_list:
        cost, current, path = heapq.heappop(open_list)
        path = path.copy()
        path.append(current)
        if current == goal:
            return path
        if current in closed_list:
            continue
        closed_list.add(current)
        for neighbor in G.neighbors(current):
            edge = (min(current, neighbor), max(current, neighbor))
            if edge not in explored_edges:
                ox.plot_graph_route(G, [current, neighbor], ax=ax, route_color='green', route_linewidth=2, route_alpha=0.5, show=False, close=False)
                explored_edges.add(edge)
                min_x = min(min_x, G.nodes[neighbor]['x'])
                max_x = max(max_x, G.nodes[neighbor]['x'])
                min_y = min(min_y, G.nodes[neighbor]['y'])
                max_y = max(max_y, G.nodes[neighbor]['y'])
                ax.set_xlim(min_x - 0.002, max_x + 0.002)
                ax.set_ylim(min_y - 0.002, max_y + 0.002)
                plt.pause(0.05)
            heapq.heappush(open_list, (cost + 1 + heuristic(neighbor, goal), neighbor, path))

def on_click(event):
    global click_count, orig, dest, ax
    click_count += 1
    nearest_node = ox.nearest_nodes(graph, X=event.xdata, Y=event.ydata)
    if click_count == 1:
        orig = nearest_node
    elif click_count == 2:
        dest = nearest_node
        click_count = 0
        find_and_plot_path()

def find_and_plot_path():
    global orig, dest, graph, ax, path_found
    plt.cla()
    ox.plot_graph(graph, ax=ax, edge_color='orange', edge_alpha=0.2, node_size=0, bgcolor='black', show=False, close=False)
    route = astar_path(graph, orig, dest)
    if route:
        ox.plot_graph_route(graph, route, route_color='red', route_linewidth=6, route_alpha=1, ax=ax, show=True, close=False)
        path_found = True
    else:
        print("No path found.")
    plt.pause(0.1)

def zoom_out():
    global ax, graph, path_found
    if path_found:
        ax.set_xlim(minx, maxx)
        ax.set_ylim(miny, maxy)
        plt.draw()


def reset():
    global click_count, orig, dest
    click_count = 0
    orig = None
    dest = None
    plt.cla()
    ox.plot_graph(graph, ax=ax, edge_color='orange', edge_alpha=0.2, node_size=0, bgcolor='black', show=False, close=False)
    plt.draw()

if __name__ == "__main__":
    north, south, east, west = 41.9171, 41.8643, 12.5004, 12.4541  
    graph = fetch_and_plot_graph_by_bbox(north, south, east, west)
    
    nodes = ox.graph_to_gdfs(graph, edges=False)
    minx, miny, maxx, maxy = nodes['x'].min(), nodes['y'].min(), nodes['x'].max(), nodes['y'].max()

    fig, ax = ox.plot_graph(graph, edge_color='orange', edge_alpha=0.2, node_size=0, bgcolor='black', show=False, close=False)
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    root = tk.Tk()
    root.title('Control Panel')
    zoom_out_button = tk.Button(root, text='Zoom Out', command=zoom_out)
    zoom_out_button.pack()
    reset_button = tk.Button(root, text='Reset', command=reset)
    reset_button.pack()
    
    fig, ax = ox.plot_graph(graph, edge_color='orange', edge_alpha=0.2, node_size=0, bgcolor='black', show=False, close=False)
    fig.canvas.mpl_connect('button_press_event', on_click)
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    manager.set_window_title('A* Pathfinding Visualization')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
    plt.margins(0, 0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    plt.show(block=False)
    root.mainloop()
