# EP3 - Automatización de Infraestructura Linux

## Descripción

Este proyecto corresponde a la Evaluación Parcial 3 (EP3) del módulo de Automatización. El objetivo es automatizar tareas de administración de sistemas Linux mediante scripts Bash, reduciendo la intervención manual y asegurando la correcta configuración de los recursos del sistema.

## Funcionalidades

- Detección automática de discos disponibles.
- Creación y configuración de particiones.
- Inicialización de volúmenes físicos (PV).
- Creación de grupos de volúmenes (VG).
- Creación de volúmenes lógicos (LV).
- Formateo de sistemas de archivos.
- Creación de directorios de montaje.
- Montaje automático y persistente mediante `/etc/fstab`.
- Validación de la configuración realizada.

## Requisitos

- Sistema operativo Linux (Red Hat Enterprise Linux 9 o compatible).
- Permisos de administrador (root o sudo).
- Herramientas LVM instaladas.
- Espacio de almacenamiento disponible para las pruebas.

## Ejecución

Asignar permisos de ejecución:

```bash
chmod +x script.sh
```

Ejecutar el script:

```bash
sudo ./script.sh
```

## Objetivo de Aprendizaje

Aplicar técnicas de automatización para la administración de almacenamiento en sistemas Linux utilizando Bash y tecnologías LVM, siguiendo buenas prácticas de administración de sistemas.

## Autor

Thomas Henriquez
