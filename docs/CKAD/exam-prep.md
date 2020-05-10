# About the exam

The exam is primarily about speed. With that in mind, the best way to approach the moderate to complex questions is to generate the initial YAML via the --dry-run flag. Then, edit the file with either vi or nano, and then create the required resource. The steps are outlined below.

```bash
$ kubectl run nginx --image=nginx --restart=Never --dry-run -o yaml > mypod.yaml
$ nano mypod.yaml
$ kubectl create -f mypod.yaml
pod "nginx" created
# There you go. If you're not satisfied with the results. Delete the resource, re-edit the declaritive yaml file, and redo.

$ kubectl delete -f mypod.yaml
pod "nginx" deleted
$ nano mypod.yaml
$ kubectl create -f mypod.yaml
pod "nginx" created
```

