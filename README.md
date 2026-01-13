kubectl apply -f argocd/application.yaml

cp -r /mnt/c/Users/nmaargade/Documents/devops_sre_poc/devops-k3s-helm-gitaction-msvc-poc ~/work/blog-poc

cd /mnt/c/Users/nmaargade/Documents/devops_sre_poc/devops-k3s-helm-gitaction-msvc-poc
kubectl apply -f argocd/application.yaml

kubectl rollout restart deployment blog -n blog

kubectl port-forward svc/blog -n blog 8081:80
kubectl port-forward svc/blog -n blog 8082:80
kubectl port-forward svc/argocd-server -n argocd 8090:443


GitHub Repo
 ├─ app/                 # Python/Go microservice
 │   ├─ Dockerfile
 │   └─ main.py | main.go
 ├─ helm/
 │   └─ myservice/
 ├─ .github/workflows/
 │   └─ ci.yml           # build + push image
 └─ argocd/
     └─ application.yaml # GitOps manifest

Developer
  ↓ git push
GitHub
  ├─ GitHub Actions (CI)
  │     └─ Build + Push Image
  ↓
Container Registry
  ↓
Argo CD (GitOps Controller)
  └─ Pulls Helm chart from Git
       ↓
K3d Kubernetes Cluster
  └─ Runs Python/Go Microservice
