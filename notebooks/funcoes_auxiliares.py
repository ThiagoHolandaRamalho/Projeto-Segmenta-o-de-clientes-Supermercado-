
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap 


import os
os.environ["OMP_NUM_THREADS"] = "1"


def graficos_elbow_silhouete(X,n_clusters = 11 ,random_state = 1):
    #Criando a análise de cotovelo(elbow) e silhouette_score 
   
    fig , axs = plt.subplots(nrows=1,ncols=2,figsize=(15,5),tight_layout =True)

    elbow = {}
    silhouet = []
    
    if isinstance(n_clusters,int):
        pass
    else:
        return 'informar um número de clusters válido'

    if n_clusters <=2:
        n_clusters = 3
    
    print(f'random_state {random_state}')
    k_range = range(2,n_clusters+1)
    X =X
    for i in k_range:
        knn = KMeans(n_clusters=i,random_state = random_state)
        knn.fit(X)
        elbow[i] = knn.inertia_
        
        labels = knn.labels_
        silhouet.append(silhouette_score(X,labels))
        
    sns.lineplot(x=list(elbow.keys()),y=elbow.values(), ax = axs[0])
    sns.lineplot(x=list(k_range),y=silhouet, ax = axs[1])

    axs[0].set_ylabel('Inertia')
    axs[0].set_xlabel('Nº Clusters')
    axs[0].set_title('Método Cotovelo')


    axs[1].set_ylabel('Silhouette Score')
    axs[1].set_xlabel('Nº Clusters')
    axs[1].set_title('Silhouette Score')

    axs[0].grid()
    axs[1].grid()
    
    plt.show()
    


#Criando uma função para o gráfico
def visualizar_cluster(df,colunas,qde_cores,centroid_pipe,coluna_cluster,centroid= True , pontos = True):
    
    #%matplotlib  ipympl
    fig = plt.figure()

    ax = fig.add_subplot(111,projection='3d')

    centroids = centroid_pipe

    cores = plt.cm.tab10.colors[:qde_cores]
    cores = ListedColormap(cores)


    x = df[colunas[0]]
    y = df[colunas[1]]
    z = df[colunas[2]]

    mostrar_centroids = centroid
    mostrar_pontos = pontos

    
    for i ,centroid in enumerate(centroids):
        
        xx,yy,zz = centroid
        if mostrar_centroids:
            ax.scatter(*centroid,s=500,alpha = 0.5)
            ax.text(xx,yy,zz,f'{i}',fontsize = 12,horizontalalignment ='center' , verticalalignment = 'center')
        
        if mostrar_pontos:
            s = ax.scatter(x,y,z,c=coluna_cluster,cmap = cores)
            ax.legend(*s.legend_elements(),bbox_to_anchor = (1.3,0.7))
        

    ax.set_xlabel(colunas[0])
    ax.set_ylabel(colunas[1])
    ax.set_zlabel(colunas[2])
    ax.set_title('Clusters')
    plt.show()