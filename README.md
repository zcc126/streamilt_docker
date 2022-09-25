dockerRegistryServiceConnection: 'c4e55f56-b26e-4b4c-981a-ec4c47c7ad9d'
imageRepository: 'zccstreamiltdocker'
containerRegistry: 'dockertestzcc.azurecr.io'

1. re-créer un pipeline à partir de Github
console Azure - service cloud Azure DevOps - Pipeline - New Pipeline - Select GitHub
2. créer un cluster AKS
services Kubernetes - créer - Intégration - Supervision de conteneur: désactiver - cluster name: testcluster1
3. configuration pipeline: Deploy to Azure Kubernetes Service
namespace: clusternamespace1 -
