# Terraform

## null_resource

[^1] A null_resource behaves exactly like any other resource, so you configure provisioners, connection details, and other meta-parameters in the same way you would on any other resource.

This is a null_resource to execute seeding logic after the database is created and for one-time use. 

```terraform
variable "password" { default = "password123" }

resource "aws_db_instance" "example" {
  allocated_storage    = 10
  storage_type         = "gp2"
  engine               = "postgres"
  instance_class       = "db.t2.micro"
  name                 = "example"
  username             = "user"
  password             = var.password
}

resource "null_resource" "seed" {
  provisioner "local-exec" {
    command = "PGPASSWORD=${var.password} psql --host=${aws_db_instance.example.address} --port=${aws_db_instance.example.port} --username=${aws_db_instance.example.username} --dbname=${aws_db_instance.example.name} < seed.sql"
  }
}
```

## depends_on

[^1] Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure. To create resources in a specific order when needed, we can use depends_on property.

```terraform
resource "null_resource" "first" {
    provisioner "local-exec" {
        command = "echo 'first'"
    }
}

resource "null_resource" "second" {
    depends_on = ["null_resource.first"]
    provisioner "local-exec" {
        command = "echo 'second'"
    }
}

resource "null_resource" "third" {
    depends_on = ["null_resource.second"]
    provisioner "local-exec" {
        command = "echo 'third'"
    }
}
```

## Targeted Changes

[^1] As your infrastructure gets more sophisticated and number of Terraform resources increases, we do not want to touch DNS or other sensitive resources while terraform apply everytime. To reduce the scope of apply, the `-target` option can be used to focus Terraform's attention on only a subset of resources. 

- This is useful when using terraform with automated deployment/delivery. When deploying multiple resources in each release, we can use null_resource along with depends_on to specify a singular resource and use 
```bash
terraform apply -target=null_resource.deployment
```


[^1]: https://medium.com/galvanize/docker-deployments-using-terraform-d2bf36ec7bdf