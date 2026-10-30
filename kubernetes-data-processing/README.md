# Kubernetes – Data Processing Application

## Descripción

Despliegue de una aplicación Flask de procesamiento de datos utilizando Kubernetes y Docker. El ejercicio implementa un Deployment con tres réplicas, configuración mediante ConfigMap y exposición interna mediante un Service ClusterIP.

## Estructura

```text
kubernetes-data-processing/
├── app/
│   ├── app.py
│   └── Dockerfile
├── k8s/
│   ├── configmap.yml
│   ├── deployment.yml
│   └── service.yml
└── README.md
```

## Implementación

**1. Construcción y carga de la imagen Docker**

```bash
docker build -t data-processing:v1 ./app
minikube image load data-processing:v1
```

**2. Aplicación de los manifiestos**

```bash
minikube kubectl -- apply -f k8s/configmap.yml
minikube kubectl -- apply -f k8s/deployment.yml
minikube kubectl -- apply -f k8s/service.yml
```

**3. Verificación del despliegue**

```bash
minikube kubectl -- get deployments
minikube kubectl -- get pods
minikube kubectl -- get services
minikube kubectl -- get endpoints data-processing-service
```

El Deployment mantiene tres réplicas de la aplicación. El contenedor utiliza variables de entorno definidas en el ConfigMap, probes de Liveness y Readiness, y límites y solicitudes de CPU y memoria.

## Pruebas adicionales

Se verificaron los siguientes mecanismos de Kubernetes:

- **Self-healing:** reemplazo automático de Pods eliminados.
- **Scaling:** modificación de la cantidad de réplicas.
- **Rolling Update:** actualización progresiva de la imagen de la aplicación.
- **Rollback:** recuperación de una versión anterior del Deployment.

Para verificar el estado de la actualización:

```bash
minikube kubectl -- rollout status deployment/data-processing
```