[Contents]
Índice de Contenidos:

  DESCRIPCIÓNDESCRIPTION
  OPCIONESOPTIONS
  IntroducciónOverview
  Soporte de RatónMouse Support

  TeclasKeys
    Otras TeclasMiscellaneous Keys
    Paneles de DirectorioDirectory Panels
    Línea de Órdenes del SistemaShell Command Line
    Teclas Generales de MovimientoGeneral Movement Keys
    Teclas de la Línea de EntradaInput Line Keys

  Barra de MenúMenu Bar
    Menús Izquierdo y Derecho (Arriba y Abajo)Left and Right Menus
      Listado...Listing Mode...
      Modo de Ordenación...Sort Order...
      Filtro...Filter...
      ReleerReread
    Menú de ArchivoFile Menu
      Cambiar de directorioQuick cd
    Menú de UtilidadesCommand Menu
      Árbol de DirectoriosDirectory Tree
      Buscar ArchivoFind File
      Búsquedas ExternasExternal panelize
      FavoritosHotlist
      Editar el Archivo de ExtensionesExtension File Edit
      Trabajos en Segundo PlanoBackground jobs
      Edición del Archivo de MenúMenu File Edit
    Menú de OpcionesOptions Menu
      ConfiguraciónConfiguration
      PresentaciónLayout
      ConfirmaciónConfirmation
      Bits de VisualizaciónDisplay bits
      Aprender teclasLearn keys
      Sistema de Archivos Virtual (VFS)Virtual FS
      Guardar ConfiguraciónSave Setup

  Ejecutando Órdenes del Sistema OperativoExecuting operating system commands
    Comando cd InternoThe cd internal command
    Sustitución de MacroMacro Substitution
    Soporte de SubshellThe subshell support
  Cambiar PermisosChmod
  Cambiar DueñoChown
  Cambiar Dueño y PermisosAdvanced Chown
  Operaciones con ArchivosFile Operations
  Copiar/Renombrar con MáscaraMask Copy/Rename
  Visor de Archivos InternoInternal File Viewer
  Editor de Archivos InternoInternal File Editor
  TerminaciónCompletion
  Sistemas de Archivos Virtuales (VFS)Virtual File System
    Sistema de archivos Tar (tarfs)Tar File System
    Sistema de archivos FTP (FTPfs)FTP File System
    Sistema de archivos de envío Archivos por SHell (FISH)FIle transfer over SHell filesystem
    Sistema de archivos de RedNetwork File System
    Sistema de archivos SMBSMB File System
    Sistema de archivos de RecuperaciónUndelete File System
    Sistema de archivos EXTerno (extfs)EXTernal File System
  ColoresColors
  Ajustes EspecialesSpecial Settings
  Ajustes del TerminalTerminal databases

  ARCHIVOS AUXILIARESFILES
  DISPONIBILIDADAVAILABILITY
  VÉASE TAMBIÉNSEE ALSO
  AUTORESAUTHORS
  ERRORESBUGS
  TRADUCCIÓNTRANSLATION
  Licencia GNULicencia GNU
  Licencia GNU (Español)Licencia GNU (Español)
  Cuadros de diálogoQueryBox
  Uso de la ayudaHow to use help
[DESCRIPTION]
DESCRIPCIÓN

"Midnight Commander" (Comandante de Medianoche) es un
navegador de directorios/gestor de archivos para sistemas
operativos tipo Unix.[OPTIONS]
OPCIONES


-a, --stickchars
        Deshabilita el uso de caracteres gráficos para el
        dibujo de líneas.

-b, --nocolor
        Fuerza el uso de la pantalla de Blanco y Negro.

-c, --color
        Fuerza el uso del modo color. Véase la sección
        ColoresColors para más información.

-C arg, --colors=arg
        Usado para especificar un juego de colores
        diferentes desde la línea de órdenes. El formato
        de arg está documentado en la sección ColoresColors.

-d, --nomouse
        Deshabilita el soporte de ratón.

-e [arch], --edit[=arch]
        Iniciar el editor interno. Si se indica un
        archivo, editarlo. Véase la página de manual de
        mcedit (1).

-f, --datadir
        Muestra las rutas de búsqueda compiladas para
        archivos de Midnight Commander.

-k, --resetsoft
        Resetea softkeys a su valor por defecto según la
        base de datos de termcap/terminfo. Sólo útil en
        terminales HP cuando la función keys no funciona.

-l reg, --ftplog=reg
        Guarda el diálogo FTPfs con el servidor en el
        archivo.

-P arch, --printwd=arch
        Al salir del programa, Midnight Commander
        registrará el último directorio de trabajo en el
        archivo indicado. Esta opción no debe ser usada
        directamente, sino desde un guión de shell
        adecuado, para dejar como directorio activo el
        directorio que estaba en uso dentro de Midnight
        Commander. Consúltese en los archivos
        /usr/share/mc/bin/mc.sh (usuarios de bash y zsh)
        y /usr/share/mc/bin/mc.csh (usuarios de tcsh) la
        manera de definir mc como un alias para el
        correspondiente guión de shell.

-s, --slow
        Activa el modo para terminales lentos. En este
        modo el programa no dibuja bordes con líneas de
        caracteres y desactiva el modo detallado.

-t, --termcap
        Usado sólo si el código fue compilado con Slang y
        terminfo: hace que Midnight Commander use el
        valor de la variable de entorno TERMCAP para
        obtener la información del terminal, en vez de la
        base de datos de terminales del sistema.

-u, --nosubshell
        Deshabilita el uso de shell concurrente (sólo
        tiene sentido si este Midnight Commander fue
        construido con soporte de shell concurrente).

-U, --subshell
        Habilita el uso de shell concurrente (sólo tiene
        sentido si este Midnight Commander fue construido
        con soporte de subshell opcional).

-v arch, --view=arch
        Iniciar el visor interno para ver el archivo
        indicado. Véase la página de manual de mcview
        (1).

-V, --version
        Muestra la versión del programa.

-x, --xterm
        Fuerza el modo xterm. Usado cuando se ejecuta en
        terminales con características de xterm (dos
        modos de pantalla, y pueden enviar secuencias de
        escape de ratón).

Si se especifica, el primer directorio se mostrará en el
panel activo y el segundo directorio en el otro panel.[Overview]
Introducción

La pantalla de Midnight Commander está divida en cuatro
partes. La mayor parte de la pantalla está ocupada por los
dos paneles de directorio. Por defecto, la segunda línea
más inferior de la pantalla es la línea de órdenes del
sistema, y la línea inferior muestra las etiquetas de las
teclas de función. La línea superior es la barra de menúMenu Bar.
La línea de la barra de menú podría no ser visible, pero
aparece si pulsamos en la primea línea de la pantalla con
el ratón o pulsamos la tecla F9.

Midnight Commander pone a la vista dos directorios al
mismo tiempo. Uno de los paneles es el panel actual (hay
una barra de selección en el panel actual). La mayoría de
las operaciones tienen lugar en el panel actual. Algunas
operaciones con archivos como Renombrar y Copiar utilizan
por defecto el directorio del panel no seleccionado como
destino, pero siempre solicitan una confirmación previa y
podemos cambiarlo. Para más información, ver las secciones
sobre los Paneles de DirectorioDirectory Panels, los Menús Izquierdo y
DerechoLeft and Right Menus y el Menú de ArchivoFile Menu.

Podemos ejecutar comandos del sistema desde el Midnight
Commander simplemente escribiéndolos. Todo lo que
escribamos aparecerá en la línea de órdenes del sistema y
cuando pulsemos Intro, Midnight Commander ejecutará estos
comandos; ver las secciones Línea de Órdenes del SistemaShell Command Line
y Teclas de la Línea de EntradaInput Line Keys para aprender más sobre
la línea de órdenes.[Mouse Support]
Soporte de Ratón

Midnight Commander soporta el uso del ratón. Se activa
cuando estamos ejecutándolo en un terminal tipo xterm(1)
(funciona incluso si realizamos una conexión de telnet,
ssh o rlogin a otra máquina desde el xterm) o si estamos
ejecutándolo en una consola Linux y tenemos el servidor
gpm cargado.

Cuando pulsamos el botón izquierdo del ratón sobre un
archivo en los paneles de directorios, ese archivo es
seleccionado; si lo hacemos con el botón derecho, el
archivo es marcado (o desmarcado, dependiendo del estado
previo).

Una doble pulsación sobre un archivo intentará ejecutar el
comando si se trata de un programa ejecutable; y si la
extensión del archivo tiene un programa asociado a esa
extensiónExtension File Edit, se ejecuta el programa especificado.

Además, es posible ejecutar los comandos asignados a las
teclas de función pulsando con el ratón sobre las
etiquetas de la línea inferior de la pantalla.

Si se pulsa un botón del ratón sobre la línea del borde
superior del panel de directorio, se sube una página hacia
atrás. Asimismo, una pulsación sobre la línea inferior
baja una página hacia adelante. Éste procedimiento vale
también para el Visor de AyudaContents y el Árbol de DirectoriosDirectory Tree.

El valor por defecto de auto repetición para los botones
del ratón es 400 milisegundos. Este valor se puede
modificar editando el archivo ~/.mc/iniSave Setup y cambiando el
parámetro mouse_repeat_rate.

Si estamos ejecutando Midnight Commander con soporte para
ratón, podemos recuperar el comportamiento habitual del
ratón (cortar y pegar texto) manteniendo pulsada la tecla
Mayúsculas.

[Keys]
Teclas

Algunos comandos en Midnight Commander implican el uso de
las teclas Control (etiquetada habitualmente CTRL o CTL) y
Meta (identificada como ALT o incluso Compose). En este
manual usaremos las siguientes abreviaturas:

C-<chr> significa mantener pulsada la tecla Control
        mientras se pulsa el carácter <chr>. Así, C-f
        sería: manteniendo pulsada la tecla Control
        teclear f.

M-<chr> significa mantener pulsada la tecla Meta o Alt
        mientras pulsamos el carácter <chr>. Si no hay
        tecla Meta o Alt, pulsar ESC, soltar, y entonces
        pulsar el carácter <chr>.

S-<chr> significa mantener pulsada la tecla de Mayúsculas
        (o Shift) y teclear <chr>.

Todas las líneas de entrada en Midnight Commander usan una
aproximación a las asociaciones de teclas del editor GNU
Emacs.

Hay bastantes secciones que hablan acerca de las teclas.
Las siguientes son las más importantes.

La sección Menú de ArchivoFile Menu documenta los atajos de
teclado para los comandos que aparecen en el Menú de
Archivo. Esta sección incluye las teclas de función. La
mayor parte de esos comandos realizan alguna acción,
normalmente sobre el archivo seleccionado o sobre los
archivos marcados.

La sección Paneles de DirectorioDirectory Panels documenta las teclas que
seleccionan un archivo o marcan archivos como objetivo de
una acción posterior (la acción normalmente es una del
menú de archivo).

La sección Línea de Órdenes del SistemaShell Command Line lista las teclas
que son usadas para introducir o editar líneas de
comandos. La mayor parte de ellas copian nombres de
archivos y demás desde los paneles de directorio a la
línea de órdenes (para evitar un tecleado excesivo) o
acceden al historial de la línea de órdenes.

Teclas de línea de EntradaInput Line Keys Son usadas para editar líneas
de entrada. Esto implica la línea de órdenes y las líneas
de entrada en las ventanas de preguntas.[Miscellaneous Keys]
Otras Teclas

Tienen cabida aquí algunas teclas que no encajan
completamente en ninguna de las anteriores categorías:

Intro. Si hay algún texto en la línea de órdenes (la de la
parte inferior de los paneles), entonces ese comando es
ejecutado. Si no hay texto en la línea de comandos
entonces si la barra de selección está situada sobre un
directorio Midnight Commander realiza un chdir(2) al
directorio seleccionado y recarga la información en el
panel; si la selección es un archivo ejecutable entonces
es ejecutado. Por último, si la extensión del archivo
seleccionado coincide con una de las extensiones en el
archivo de extensionesExtension File Edit entonces se ejecuta la aplicación
correspondiente.

C-l     redibuja toda la pantalla de Midnight Commander.

C-x c   Cambiar PermisosChmod de un archivo o un conjunto de
        archivos marcados.

C-x o   Cambiar DueñoChown del archivo actual o de los
        archivos marcados.

C-x l   crea enlaces.

C-x s   crea enlaces simbólicos.

C-x C-s edita enlaces simbólicos.

C-x i   cambia el panel opuesto al modo de información.

C-x q   cambia el panel opuesto al modo de vista rápida.

C-x !   ejecuta Búsquedas ExternasExternal panelize.

C-x h   añade el sitio actual a la lista de FavoritosHotlist.

M-!     ejecuta una orden del sistema y muestra su salida
        en el Visor de Archivos InternoInternal File Viewer.

M-?     Buscar ArchivoFind File.

M-c     permite Cambiar de DirectorioQuick cd.

C-o     en la consola de Linux o FreeBSD o bajo un xterm,
        se muestra la salida de la orden anterior. En la
        consola de Linux, Midnight Commander usa un
        programa externo (cons.saver) para controlar la
        copia y restauración de la pantalla.

Cuando se haya creado Midnight Commander con soporte de
subshell incluido, podemos pulsar C-o en cualquier momento
y volver a la pantalla principal; para volver a nuestra
aplicación bastará con volver a pulsar C-o. Si tenemos una
aplicación suspendida en esta situación, no podremos
ejecutar otros programas desde Midnight Commander hasta
que terminemos la aplicación suspendida.[Directory Panels]
Paneles de Directorio

Esta sección enumera las teclas que operan en los paneles
de directorio. Si queremos saber cómo cambiar la
apariencia de los paneles, deberemos echar un vistazo a la
sección Menús Izquierdo y DerechoLeft and Right Menus.

Tab, C-i
        cambia el panel actual. El panel activo deja de
        serlo y el no activo pasa a ser el nuevo panel
        activo. La barra de selección se mueve del
        antiguo panel al nuevo, desaparece de aquel y
        aparece en éste.

Insertar, C-t
        para marcar archivos (y/o directorios) como
        seleccionados podemos usar la tecla Insertar
        (Ins) (La secuencia kich1 de terminfo) o la
        combinación C-t (Control-t). Para deseleccionar
        archivos, basta con repetir la operación sobre
        los archivos y/o directorios antes marcados.

M-g, M-r, M-j
        usadas para seleccionar el archivo superior en un
        panel, el archivo central y el inferior del
        panel, respectivamente.

C-s, M-s
        inicia la búsqueda de un archivo en la lista de
        directorios (panel activo). Cuando la búsqueda
        está activa las pulsaciones de teclado son
        añadidas a la cadena de búsqueda y no a la línea
        de órdenes. Si la opción Mostrar Mini-estado está
        habilitada la cadena a buscar es mostrada en la
        línea de mini-estado. Conforme tecleemos, la
        barra de selección se desplazará al siguiente
        archivo o directorio cuyo nombre coincida con las
        letras introducidas. Las teclas borrar o suprimir
        pueden ser utilizadas para corregir errores de
        escritura. Si pulsamos C-s de nuevo, se busca la
        siguiente coincidencia.

M-t     rota el listado de pantalla actual para mostrar
        el siguiente modo de listado. Con esto es posible
        intercambiar rápidamente de un listado completo
        al regular o breve, así como al modo de listado
        definido por el usuario.

C-\ (control-Contrabarra)
        muestra la lista de sitios FavoritosHotlist y permite
        cambiar al directorio seleccionado. * N. de T.:
        En el teclado castellano, existe un pequeño
        inconveniente, dado que la contrabarra, no se
        consigue con una sola pulsación, por lo que este
        método no funciona directamente.

+ (más) usado para seleccionar (marcar) un grupo de
        archivos. Midnight Commander preguntará por una
        expresión regular describiendo el grupo. Cuando
        los Caracteres Comodín (Shell Patterns) están
        habilitados, la expresión regular es idéntica a
        las expresiones regulares en el shell (poniendo *
        para cero o más caracteres y ? para uno o más
        caracteres). Si los Caracteres Comodín están
        deshabilitados, entonces la selección de archivos
        se realiza con expresiones regulares normales
        (VA. ed (1)).

        Si la expresión empieza o termina con una barra
        (/), entonces la selección se realiza sobre
        directorios en vez de archivos.

- (menos) o \ (contrabarra)
        usaremos la tecla - o "\" para deseleccionar un
        grupo de archivos. Ésta es la operación contraria
        a la realizada por la tecla Más (+). * N. de T.:
        La tecla que realiza originalmente la función
        descrita es el menos (-) ya que ésta es la
        utilizada en la versión originaria del programa,
        Comandante Norton.

Cursor-Arriba, C-p
        desplaza la barra de selección a la entrada
        anterior en el panel.

Cursor-Abajo, C-n
        desplaza la barra de selección a la entrada
        siguiente en el panel.

Inicio (Home), a1, M-<
        desplaza la barra de selección a la primera
        entrada en el panel.

Fin (End), c1, M->
        desplaza la barra de selección a la última
        entrada en el panel.

Av. Pág (next-page), C-v
        desplaza la barra de selección a la página
        siguiente.

Re. Pág (prev-page), M-v
        desplaza la barra de selección a la página
        anterior.

M-o     si el otro panel es un panel con lista de
        archivos y estamos situados en un directorio en
        el panel activo actual, entonces otro panel se
        posiciona dentro del directorio del panel activo
        (como la tecla de Emacs C-o) en otro caso el otro
        panel es posicionado el directorio padre del
        directorio seleccionado en el panel activo.

C-RePág (C-PageUp), C-AvPág (C-PageDown)
        solamente bajo la consola Linux: realiza un chdir
        ".." o al directorio actualmente seleccionado
        respectivamente.[Shell Command Line]
Línea de Órdenes del Sistema

Esta sección enumera las teclas útiles para evitar la
excesiva escritura cuando se introducen órdenes del
sistema.

M-Intro copia el nombre de archivo seleccionado a la
        línea de órdenes.

C-Intro igual que M-Intro. Puede no funcionar en ciertos
        sistemas o con algunos terminales.

C-S-Intro
        copia la ruta completa del archivo actual en la
        línea de órdenes. Puede no funcionar en ciertos
        sistemas o con algunos terminales.

M-Tab   realiza una Terminación automática (completion)Completion
        del nombre de archivo, comando, variable, nombre
        de usuario y host.

C-x t, C-x C-t
        copia los archivos marcados (o si no los hay, el
        archivo seleccionado) del panel activo (C-x t) o
        del otro panel (C-x C-t) a la línea de órdenes.

C-x p, C-x C-p
        la primera secuencia de teclas copia el nombre de
        la ruta de acceso actual a la línea de órdenes, y
        la segunda copia la ruta del otro panel a la
        línea de órdenes.

C-q     el comando cita (quote) puede ser utilizado para
        insertar caracteres que de otro modo serían
        interpretados por Midnight Commander (como el
        símbolo '+')

M-p, M-n
        usaremos esas teclas para navegar a través del
        histórico de comandos. M-p devuelve la última
        entrada, M-n devuelve la siguiente.

M-h     visualiza el historial para la línea de entrada
        actual.[General Movement Keys]
Teclas Generales de Movimiento

El visor de ayuda, el visor de archivo y el árbol de
directorios usan un código de control de movimiento común.
Por consiguiente, reconocen las mismas teclas. Además,
cada uno reconoce algunas otras teclas propias.

Otras partes de Midnight Commander utilizan algunas de las
mismas teclas de movimiento, por lo que esta sección
podría ser aplicada a ellas también.

Arriba (Up), C-p
        mueve una línea hacia arriba.

Abajo (Down), C-n
        mueve una línea hacia abajo.

Re Pág (Retroceso de Página, Prev Page, Page Up), M-v
        mueve una página completa hacia atrás.

Av Pág (Avance de Página, Next Page, Page Down), C-v
        mueve una página hacia delante.

Inicio (Home), A1
        mueve al principio.

Fin (End), C1
        mueve al final.

El visor de ayuda y el de archivo reconocen las siguientes
teclas aparte de las mencionadas anteriormente:

b, C-b, C-h, Retroespacio (Backspace), Suprimir (Delete)
        mueve una página completa hacia atrás.

Barra espaciadora (Space bar)
        mueve una página hacia delante.

u, d    mueve la mitad de la página hacia atrás o
        adelante.

g, G    mueve al principio o al final.[Input Line Keys]
Teclas de la Línea de Entrada

Las líneas de entrada (usadas en la línea de órdenesShell Command Line y
para los cuadros de diálogo en el programa) reconocen esas
teclas:

C-a     coloca el cursor al comienzo de la línea.

C-e     coloca el cursor al final de la línea.

C-b, Izquierda (move-left)
        desplaza el cursor una posición a la izquierda.

C-f, Derecha (move-right)
        desplaza el cursor una posición a la derecha.

M-f     avanza una palabra.

M-b     retrocede una palabra.

C-h, Retroespacio (backspace)
        borra el carácter anterior.

C-d, Suprimir (Delete)
        elimina el carácter de la posición del cursor.

C-@     sitúa una marca para cortar.

C-w     copia el texto entre el cursor y la marca a la
        caché de eliminación y elimina el texto de la
        línea de entrada.

M-w     copia el texto entre el cursor y la marca a la
        caché de eliminación.

C-y     restaura el contenido de la caché de eliminación.

C-k     elimina el texto desde el cursor hasta el final
        de la línea.

M-p, M-n
        usaremos esas teclas para desplazarnos a través
        del historial de comandos. M-p nos lleva a la
        última entrada, M-n nos sitúa en la siguiente.

M-C-h, M-Retroespacio (M-Backspace)
        borra la palabra anterior.

M-Tab   realiza una terminaciónCompletion del nombre de archivo,
        comando, variable, nombre de usuario o host.

[Menu Bar]
Barra de Menú

La barra de menú aparece cuando pulsamos F9 o pulsamos el
botón del ratón sobre la primera fila de la pantalla. La
barra de menú tiene cinco submenús: "Izquierdo",
"Archivo", "Utilidades", "Opciones" y "Derecho".

Los Menús Izquierdo y DerechoLeft and Right Menus nos permiten modificar la
apariencia de los paneles de directorio izquierdo y
derecho.

El Menú de ArchivoFile Menu lista las acciones que podemos
realizar sobre el archivo actualmente seleccionado o sobre
los archivos marcados.

El Menú de UtilidadesCommand Menu lista las acciones más generales y
que no guardan relación con la selección actual de
archivos.[Left and Right Menus]
Menús Izquierdo y Derecho (Arriba y Abajo)

La presentación de los paneles de directorio puede ser
cambiada desde los menús Izquierdo y Derecho (denominados
Arriba y Abajo si hemos elegido la disposición horizontal
de paneles en las opciones de presentaciónLayout).[Listing Mode...]
Listado...

La vista en modo "Listado" se usa para mostrar la lista de
archivos. Hay cuatro modos disponibles: Completo, Breve,
Largo, y Definido por el usuario.

En modo completo se muestra el nombre del archivo, su
tamaño y la fecha y hora de modificación.

Breve muestra sólo los nombres de archivo, en dos
columnas. Esto permite ver el doble de entradas que en los
otros modos.

El modo largo es similar a la salida de la orden ls -l.
Este modo requiere todo el ancho de la pantalla.

Si se elige el modo definido por el usuario, hay que
especificar el formato de presentación. Un formato
personalizado tiene que comenzar con la indicación de
tamaño de panel, que puede ser "half" (medio) o "full"
(completo) para tener respectivamente dos paneles de media
pantalla o un único panel a pantalla completa. Tras el
tamaño se puede colocar el número "2" para dividir el
panel en dos columnas.

A continuación van los campos deseados con especificación
opcional del tamaño. Los campos que se pueden emplear son:

name    nombre del archivo.

size    tamaño del archivo.

bsize   forma alternativa para size. Muestra el tamaño de
        los archivos y SUB-DIR o DIR-ANT para
        directorios.

type    carácter de tipo de archivo. Este carácter se
        asemeja a lo mostrado por la orden ls -F: * para
        archivos ejecutables, / para directorios, @ para
        enlaces, = para sockets, - para los dispositivos
        en modo carácter, + para dispositivos en modo
        bloque, | para tuberías, ~ para enlaces
        simbólicos a directorios y ! para enlaces rotos
        (enlaces que no apuntan a nada).

mark    un asterisco si el archivo está marcado, o un
        espacio si no lo está.

mtime   fecha y hora de la última modificación del
        contenido del archivo.

atime   fecha y hora del último acceso al archivo.

ctime   fecha y hora del último cambio del archivo.

perm    cadena representando los permisos del archivo.

mode    valor en octal representando los permisos del
        archivo.

nlink   número de enlaces al archivo.

ngid    Identificador de Grupo, GID (numérico).

nuid    Identificador de Usuario, UID (numérico).

owner   propietario del archivo.

group   grupo del archivo.

inode   número de inodo del archivo.

Además, podemos ajustar la apariencia del panel con:

space   un espacio.

|       añadir una línea vertical.

Para fijar el tamaño de un campo basta añadir : seguido
por el número de caracteres que se desee. Si tras el
número colocamos el símbolo + el tamaño indicado será el
tamaño mínimo, y si hay espacio de sobra se extenderá más
el campo.

Como ejemplo, el listado Completo corresponde al formato:

half type name | size | mtime

Y el listado Largo corresponde a:

full perm space nlink space owner space group space size
space mtime space name

Éste es un bonito formato de pantalla definido por el
usuario:

half name | size:7 | type mode:3

Los paneles admiten además los siguientes modos:

"Información"
        La vista de información muestra detalles
        relativos al archivo seleccionado y, si es
        posible, sobre el sistema de archivos usado.

"Árbol" La vista en árbol es bastante parecida a la
        utilidad árbol de directoriosDirectory Tree. Para más
        información véase la sección correspondiente.

"Vista Rápida"
        En este modo, en el panel aparece visorInternal File Viewer
        reducido que muestra el contenido del archivo
        seleccionado. Si se activa el panel (con el
        tabulador o con el ratón), se dispone de los
        funciones usuales del visor.[Sort Order...]
Modo de Ordenación...

Los ocho modos de ordenación son por nombre, por
extensión, por hora de modificación, por hora de acceso,
por la hora de modificación de la información del inodo,
por tamaño, por inodo y desordenado. En el cuadro de
diálogo del modo de ordenación podemos elegir el modo de
ordenación así como especificar si deseamos que éste se
realice en orden inverso chequeando la casilla Invertir.

Por defecto, los directorios se colocan ordenados antes
que los archivos. Esto se puede cambiar en Configuración
dentro del Menú de OpcionesOptions Menu activando la opción Mezclar
archivos y directorios.[Filter...]
Filtro...

La utilidad filtro nos permite seleccionar con un patrón
(por ejemplo *.tar.gz) los archivos a listar. Indiferentes
al patrón de filtro, siempre se muestran todos los
directorios y enlaces a directorios.[Reread]
Releer

El comando releer recarga la lista de archivos en el
directorio. Esto es útil si otros procesos han creado,
borrado o modificado archivos. Si hemos panelizado los
nombres de los archivos en un panel, esto recargará los
contenidos del directorio y eliminará la información
panelizada (véase la sección Búsquedas externasExternal panelize para más
información).[File Menu]
Menú de Archivo

Midnight Commander utiliza las teclas de función F1 - F10
como atajos de teclado para los comandos que aparecen en
el menú de archivo. Las secuencias de escape para las
Fkeys son características de terminfo desde kf1 hasta
kf10. En terminales sin soporte de teclas de función,
podemos conseguir la misma funcionalidad pulsando la tecla
ESC seguido de un número entre 1 y 9 ó 0 (correspondiendo
a las teclas F1 a F9 y F10 respectivamente).

El menú de Archivo recoge las siguientes opciones (con los
atajos de teclado entre paréntesis):

Ayuda (F1)

Invoca el visor hipertexto de ayuda interno. Dentro del
visor de ayudaContents, podemos usar la tecla Tab para seleccionar
el siguiente enlace y la tecla Intro para seguir ese
enlace. Las teclas Espacio y Retroespacio son usadas para
mover adelante y atrás en una página de ayuda. Pulsando F1
de nuevo para obtener la lista completa de teclas válidas.

Menú de Usuario (F2)

Invoca el Menú de usuarioMenu File Edit El menú de usuario otorga una
manera fácil de tener usuarios con un menú y añadir
asimismo características extra a Midnight Commander.

Ver (F3, S-F3)

Visualiza el archivo seleccionado. Por defecto invoca el
Visor de Archivos InternoInternal File Viewer pero si la opción "Usar visor
interno" está desactivada, invoca un visor de archivos
externo especificado por la variable de entorno PAGER. Si
la variable PAGER no está definida, se invoca al comando
"view". Si en vez de esto usamos S-F3, el visor será
invocado sin realizar ningún tipo de formateo o
preprocesamiento del archivo.

Ejecutar y Ver (M-!)

El comando con los argumentos indicados se ejecuta, y la
salida se muestra usando el visor de archivos interno.
Como argumento se ofrece, por defecto, el nombre
seleccionado en el panel.

Editar (F4)

Invoca el editor vi, u otro especificado en la variable de
entorno EDITOR, o el Editor de Archivos InternoInternal File Editor si la
opción use_internal_edit está activada.

Copiar (F5)

Sobreimpresiona una ventana de entrada con destino por
defecto al directorio del panel no seleccionado y copia el
archivo actualmente seleccionado (o los archivos marcados,
si hay al menos uno marcado) al directorio especificado
por el usuario en la ventana. Durante este proceso,
podemos pulsar C-c o ESC para anular la operación. Para
más detalles sobre la máscara de origen (que será
normalmente * o ^\(.*\)$ dependiendo de la selección de
Uso de los patrones del shell) y los posibles comodines en
destino véase Máscara copiar/renombrarMask Copy/Rename.

En algunos sistemas, es posible hacer la copia en segundo
plano pulsando en el botón de segundo plano con el ratón
(o pulsando M-b en el cuadro de diálogo). Los Trabajos en
Segundo PlanoBackground jobs son utilizados para controlar los procesos
en segundo plano.

Crear Enlace (C-x l)

Crea un enlace al archivo actual.

Crear Enlace Simbólico (C-x s)

Crea un enlace simbólico al archivo actual. Para aquellos
que no conozcan qué son los enlaces: crear un enlace a un
archivo es algo parecido a copiar el archivo, salvo que el
archivo original y el destino representan el mismo archivo
físico, los mismos datos reales. Por ejemplo, si editamos
uno de esos archivos, todos los cambios que realicemos
aparecerán en ambos archivos. Hay quien llama a los
enlaces alias o accesos directos.

Un enlace aparece como un archivo real. Después de
crearlo, no hay modo de decir cuál es el original y cuál
el enlace. Si borramos uno de ellos el otro aún seguirá
intacto. Es muy difícil advertir que los archivos
representan la misma imagen. Usaremos estos enlaces cuando
no necesitemos saberlo.

Un enlace simbólico es una referencia al nombre del
archivo original. Si el archivo original es borrado, el
enlace simbólico queda sin utilidad. Es bastante fácil
advertir que los archivos representan la misma imagen.
Midnight Commander muestra un símbolo "@" delante del
nombre del archivo si es un enlace simbólico a alguna
parte (excepto a un directorio, caso en que muestra una
tilde (~)). El archivo original al cual el enlace apunta
es mostrado en la línea de estado si la opción "Mini
status" está habilitada. Usaremos enlaces simbólicos
cuando queramos evitar la confusión que pueden causar los
enlaces físicos.

Renombrar/Mover (F6)

Presenta un diálogo de entrada proponiendo como directorio
de destino el directorio del panel no activo, y mueve
allí, o bien los archivos marcados o en su defecto el
archivo seleccionado. El usuario puede introducir en el
diálogo un destino diferente. Durante el proceso, se puede
pulsar C-c o ESC para abortar la operación. Para más
detalles, véase más arriba la operación Copiar, dado que
la mayoría de los aspectos son similares.

En algunos sistemas, es posible hacer la copia en segundo
plano pulsando con el ratón en el susodicho botón de
segundo plano (o pulsando M-o en el cuadro de diálogo).
Con Procesos en 2º planoBackground jobs se puede controlar estas tareas.

Crear Directorio (F7)

Presenta un diálogo de entrada y crea el directorio
especificado.

Borrar (F8)

Borra, o bien los archivos marcados o en su defecto el
archivo seleccionado en el panel activo. Durante el
proceso, se puede pulsar C-c o ESC para abortar la
operación.

Cambiar Directorio (M-c) Usaremos el comando Cambiar de
directorioQuick cd si tenemos llena la línea de órdenes y
queremos hacer un cd a algún lugar.

Seleccionar Grupo (+)

Es usado para seleccionar (marcar) un grupo de archivos.
Midnight Commander preguntará por una expresión regular
describiendo el grupo. Cuando los Patrones del Shell están
habilitados, la expresión regular es tal y como lo es en
el shell (* para cero o más caracteres y ? para un
carácter). Si los Patrones del Shell están desactivados,
entonces la selección de archivos se realiza con
expresiones regulares normales (Véase ed (1)).

Para marcar directorios en vez de archivos, la expresión
debe empezar o terminar con '/'.

De-seleccionar Grupo (\)

Utilizado para deseleccionar un grupo de archivos. Es la
operación antagonista al comando Selecciona grupo.

Salir (F10, S-F10)

Finaliza Midnight Commander. S-F10 es usado cuando
queremos salir y estamos utilizando la envoltura del
shell. S-F10 no nos llevará al último directorio visitado
con Midnight Commander, en vez de eso nos llevará al
directorio donde fue invocado Midnight Commander.[Quick cd]
Cambiar de directorio

Este comando es útil si tenemos completa la línea de
órdenes y queremos hacer un cdThe cd internal command a algún lugar sin tener
que cortar y pegar sobre la línea. Este comando
sobreimpresiona una pequeña ventana, donde introducimos
todo aquello que es válido como argumento del comando cd
en la línea de órdenes y después pulsamos intro. Este
comando caracteriza todas las cualidades incluidas en el
comando cd internoThe cd internal command.[Command Menu]
Menú de Utilidades

Árbol de directoriosDirectory Tree muestra una figura con estructura de
árbol con los directorios.

Buscar archivoFind File permite buscar un archivo específico. El
comando "Intercambiar paneles" intercambia los contenidos
de los dos paneles de directorios.

El comando "Activa/desactiva paneles" muestra la salida
del último comando del shell. Esto funciona sólo en xterm
y en una consola Linux y FreeBSD.

El comando Compara directorios (C-x d) compara los paneles
de directorio uno con el otro. Podemos usar el comando
Copiar (F5) para hacer ambos paneles idénticos. Hay tres
métodos de comparación. El método rápido compara sólo el
tamaño de archivo y la fecha. El método completo realiza
una comparación completa octeto a octeto. El método
completo no está disponible si la máquina no soporta la
llamada de sistema mmap(2). El método de comparación de
sólo tamaño sólo compara los tamaños de archivo y no
chequea los contenidos o las fechas, sólo chequea los
tamaños de los archivos.

El comando Histórico de comandos muestra una lista de los
comandos escritos. El comando seleccionado es copiado a la
línea de órdenes. El histórico de comandos puede ser
accedido también tecleando M-p ó M-n.

Favoritos (C-\)Hotlist permite acceder con facilidad a
directorios y sitios utilizados con frecuencia.

Búsquedas ExternasExternal panelize nos permite ejecutar un programa
externo, y llevar la salida de ese programa al panel
actual.

Editar el archivo de extensionesExtension File Edit nos permite especificar
los programas a ejecutar para intentar ejecutar, ver,
editar y realizar un montón de cosas sobre archivos con
ciertas extensiones (terminaciones de archivo). Por
ejemplo, asociar la extensión de los archivos de audio de
SUN (.au) con el programa reproductor adecuado. Editar
archivo de menúMenu File Edit se puede utilizar para editar el menú de
usuario (el que aparece al pulsar F2).[Directory Tree]
Árbol de Directorios

El comando Árbol de directorios muestra una figura con la
estructura de los directorios. Podemos seleccionar un
directorio de la figura y Midnight Commander cambiará a
ese directorio.

Hay dos modos de invocar el árbol. El comando de árbol de
directorios está disponible desde el menú Utilidades. El
otro modo es seleccionar la vista en árbol desde el menú
Izquierdo o Derecho.

Para evitar largos retardos Midnight Commander crea la
figura de árbol escaneando solamente un pequeño
subconjunto de todos los directorios. Si el directorio que
queremos ver no está, nos moveremos hasta su directorio
padre y pulsaremos C-r (o F2).

Podemos utilizar las siguientes teclas:

Teclas de Movimiento GeneralGeneral Movement Keys válidas.

Intro. En el árbol de directorios, sale del árbol de
directorios y cambia al directorio en el panel actual. En
la vista de árbol, cambia a este directorio en el otro
panel y permanece en el modo de vista Árbol en el panel
actual.

C-r, F2 (Releer). Relee este directorio. Usaremos este
comando cuando el árbol de directorios esté anticuado: hay
directorios perdidos o muestra algunos directorios que no
existen ya.

F3 (Olvidar). Borra ese directorio de la figura del árbol.
Usaremos esto para eliminar desorden de la figura. Si
queremos que el directorio vuelva a la figura del árbol
pulsaremos F2 en su directorio padre.

F4 (Estático/Dinámico, Dinam/Estát). Intercambia entre el
modo de navegación dinámico (predefinido) y el modo
estático.

En el modo de navegación estático podemos usar las teclas
del cursor Arriba y Abajo para seleccionar un directorio.
Todos los directorios conocidos serán mostrados.

En el modo de navegación dinámico podemos usar las teclas
del cursor Arriba y Abajo para seleccionar el directorio
hermano, la tecla Izquierda para situarnos en el
directorio padre, y la tecla Derecha para situarnos en el
directorio hijo. Sólo los directorios padre, hijo y
hermano son mostrados, el resto son dejados fuera. La
figura de árbol cambia dinámicamente conforme nos
desplazamos sobre ella.

F5 (Copiar). Copia el directorio.

F6 (Renombrar/Mover, RenMov). Mueve el directorio.

F7 (Mkdir). Crea un nuevo directorio por debajo del
directorio actual. El directorio creado será así el hijo
del directorio del cual depende jerárquicamente (Padre).

F8 (Eliminar). Elimina este directorio del sistema de
archivos.

C-s, M-s. Busca el siguiente directorio coincidente con la
cadena de búsqueda. Si no hay tal directorio esas teclas
moverán una línea abajo.

C-h, Retroespacio. Borra el último carácter de la cadena
de búsqueda.

Cualquier otro carácter. Añade el carácter a la cadena de
búsqueda y se desplaza al siguiente directorio que
comienza con esos caracteres. En la vista de árbol debemos
primero activar el modo de búsqueda pulsando C-s. La
cadena de búsqueda es mostrada en la línea de mini-estado.

Las siguientes acciones están disponibles sólo en el árbol
de directorios. No son funcionales en la vista de árbol.

F1 (Ayuda). Invoca el visor de ayuda y muestra ésta
sección.

Esc, F10. Sale del árbol de directorios. No cambia el
directorio.

El ratón es soportado. Un doble Click se comporta como
pulsar Intro. Véase también la sección sobre soporte de
ratónMouse Support.[Find File]
Buscar Archivo

La opción Buscar Archivo primero pregunta por el
directorio inicial para la búsqueda y el nombre de archivo
a buscar. Pulsando el botón árbol podemos seleccionar el
directorio inicial desde el Árbol de directoriosDirectory Tree.

El campo de contenidos acepta expresiones regulares
similares a egrep(1). Eso significa que tenemos caracteres
de escape con significado especial para egrep con "\",
p.e. si buscamos "strcmp (" tendremos que introducir
"strcmp \(" (sin las dobles comillas).

Podemos iniciar la búsqueda pulsando el botón Aceptar.
Durante el proceso de búsqueda podemos detenerla desde el
botón Terminar.

Podemos navegar por la lista de archivos con las teclas
del cursor Arriba y Abajo. El botón Chdir cambiará al
directorio del archivo actualmente seleccionado. El botón
"Otra vez" preguntará los parámetros para una nueva
búsqueda. El botón Terminar finaliza la operación de
búsqueda. El botón Panelizar colocará los archivos
encontrados en el panel actual y así podremos realizar más
operaciones con ellos (ver, copiar, mover, borrar y
demás). Después de panelizar podemos pulsar C-r para
regresar al listado normal de archivos.

Es posible tener una lista de directorios que el comando
Buscar Archivo debería saltar durante la búsqueda (por
ejemplo, podemos querer evitar búsquedas en un CDROM o en
un directorio NFS que está montado a través de un enlace
lento).

Los directorios a ser omitidos deberían ser enumerados en
la variable find_ignore_dirs en la sección Misc de nuestro
archivo ~/.mc/ini.

Los componentes del directorio deberían ser separados por
dos puntos, como en el ejemplo que sigue:

[Misc]
find_ignore_dirs=/cdrom:/nfs/wuarchive:/afs

Debemos valorar la utilización de Búsquedas externasExternal panelize en
ciertas situaciones. La utilidad Buscar archivos es sólo
para consultas simples, pero con Búsquedas externas se
pueden hacer exploraciones tan complejas como queramos.[External panelize]
Búsquedas Externas

Búsquedas externas nos permite ejecutar un programa
externo, y tomar la salida de ese programa como contenido
del panel actual.

Por ejemplo, si queremos manipular en uno de los paneles
todos los enlaces simbólicos del directorio actual,
podemos usar búsquedas externas para ejecutar el siguiente
comando:

find . -type l -print

Hasta la finalización del comando, el contenido del
directorio del panel no será el listado de directorios del
directorio actual, pero sí todos los archivos que son
enlaces simbólicos.

Si queremos panelizar todos los archivos que hemos bajado
de nuestro servidor ftp, podemos usar el comando awk para
extraer el nombre del archivo de los archivos de registro
(log) de la transferencia:

awk '$9 ~! /incoming/ { print $9 }' < /usr/adm/xferlog

Tal vez podríamos necesitar guardar los comandos
utilizados frecuentemente bajo un nombre descriptivo, de
manera que podamos llamarlos rápidamente. Haremos esto
tecleando el comando en la línea de entrada y pulsando el
botón "Añadir nuevo". Entonces introduciremos un nombre
bajo el cual queremos que el comando sea guardado. La
próxima vez, bastará elegir ese comando de la lista y no
habrá que escribirlo de nuevo.[Hotlist]
Favoritos

Muestra una lista de sitios y directorios guardados y abre
en el panel el lugar seleccionado. Desde el cuadro de
diálogo podemos también crear y eliminar entradas. Para
añadir se puede igualmente utilizar Añadir Actual (C-x h),
que añade el directorio actual (no el seleccionado) a la
lista de favoritos. Se pide al usuario una etiqueta para
identificar la entrada.

Esto hace más rápido el posicionamiento en los directorios
usados frecuentemente. Deberíamos considerar también el
uso de la variable CDPATH tal y como se describe en
comando cd internoThe cd internal command.[Extension File Edit]
Editar el Archivo de Extensiones

Abre el archivo ~/.mc/bindings en nuestro editor. El
administrador puede optar por editar, en su lugar, el
archivo de extensiones del sistema /usr/share/mc/mc.ext.
El formato del archivo (formato nuevo cambiado desde la
versión 3.0) es como sigue:

Todas las líneas que empiecen con # o estén vacías serán
ignoradas.

Las líneas que comiencen en la primera columna deberán
tener el siguiente formato:

PalabraClave/Descripción+NuevaLínea, p.e. cualquier cosa
después de palabraClave/ hasta el fin de línea es
descripción

las palabras clave son:

shell   (desc es entonces cualquier extensión (sin
        comodines), p.e. para indicar todos los archivos
        con extensión desc (*desc). Ejemplo: .tar indica
        *.tar)

regex   (desc es una expresión regular)

type    (el archivo coincide si `file %f` coincide con la
        expresión regular indicada en desc (el nombre de
        archivo: parte de `file %f` es eliminada))

default (coincide con todo archivo sin importar su
        descripción)

El resto de líneas deben comenzar con un espacio o
tabulador y usar el siguiente formato:
PalabraClave=comando+NuevaLínea (sin espacios junto al =),
donde PalabraClave debe ser: Open (si el usuario pulsa
Intro o dos veces el ratón), View (F3) o Edit (F4).
comando es cualquier comando en línea del shell, con
sustitución de macroMacro Substitution simple.

Las reglas se aplican en estricto orden. Aunque se
produzca una coincidencia, si la acción solicitada no está
disponible, se ignora y la búsqueda continúa (por ejemplo,
si un archivo encaja con dos entradas, pero la acción Ver
no está definida en la primera, al pulsar F3, se ejecuta
la acción Ver de la segunda). Como último recurso default
debe incluir todas las acciones.[Background jobs]
Trabajos en Segundo Plano

Nos permite controlar el estado de cualquier proceso de
Midnight Commander en segundo plano (sólo las operaciones
de copiar y mover archivos pueden realizarse en segundo
plano). Podemos parar, reiniciar y eliminar procesos en
segundo plano desde aquí.[Menu File Edit]
Edición del Archivo de Menú

El menú de usuario es un menú de acciones útiles que puede
ser personalizado por el usuario. Cuando accedemos al menú
de usuario se utiliza, si existe, el archivo .mc.menu del
directorio actual, pero sólo si es propiedad del usuario o
del superusuario y no es modificable por todos. Si no se
encuentra allí el archivo, se intenta de la misma manera
con ~/.mc/menu, y si no, mc utiliza el menú por defecto
para todo el sistema /usr/share/mc/mc.menu.

El formato del menú de archivo es muy simple. Las líneas
que empiezan con todo excepto espacio o tab son
consideradas entradas para el menú (para posibilitar su
uso como atajo de teclado, el primer carácter deberá ser
una letra). Todas las líneas que comienzan con tab o
espacio son los comandos que serán ejecutados cuando la
entrada es seleccionada.

Cuando se selecciona una opción todas las líneas de
comandos de la opción se copian a un archivo temporal del
directorio homónimo (normalmente /usr/tmp) y entonces es
ejecutado el archivo. Esto permite al usuario poner
constructores normales del shell en los menús. También
tiene lugar una sustitución simple de macros antes de
ejecutar el código del menú. Para mayor información, ver
Sustitución de macroMacro Substitution.

He aquí un ejemplo de archivo mc.menu:

A	Vuelca el contenido del archivo seleccionado
	od -c %f

B	Edita un informe de errores y lo envía al superusuario
	I=`mktemp ${MC_TMPDIR:-/tmp}/mail.XXXXXX` || exit 1
	vi $I
	mail -s "Error Midnight Commander" root < $I
	rm -f $I

M	Lee al correo
	emacs -f rmail

N	Lee las noticias de Usenet
	emacs -f gnus

H	Realiza una llamada al navegador hypertexto info
	info

J	Copia recursivamente el directorio actual al otro panel
	tar cf - . | (cd %D && tar xvpf -)

K	Realiza una versión del directorio actual
	echo -n "Nombre del archivo de distribución: "
	read tar
	ln -s %d `dirname %d`/$tar
	cd ..
	tar cvhf ${tar}.tar $tar

= f *.tar.gz | f *.tgz & t n
X       Extrae los contenidos de un archivo tar comprimido
	tar xzvf %f

Condiciones por Defecto

Cada entrada del menú puede ir precedida por una
condición. La condición debe comenzar desde la primera
columna con un carácter '='. Si la condición es verdadera,
la entrada del menú será la entrada por defecto.

Sintaxis condicional: 	= <sub-cond>
  o:			= <sub-cond> | <sub-cond> ...
  o:			= <sub-cond> & <sub-cond> ...

Sub-condición es una de las siguientes:

  f <patrón>		¿el archivo actual encaja con el patrón?
  F <patrón>		¿otro archivo encaja con el patrón?
  d <patrón>		¿el directorio actual encaja con el patrón?
  D <patrón>		¿otro directorio encaja con el patrón?
  t <tipo>		¿archivo actual es de tipo <tipo>?
  T <tipo>		¿otro archivo es de tipo <tipo>?
  ! <sub-cond>		niega el resultado de la sub-condición

Patrón es un patrón normal del shell o una expresión
regular, de acuerdo con la opción de patrones del shell.
Podemos cambiar el valor global de la opción de los
patrones del shell escribiendo "shell_patterns=x" en la
primera línea del archivo de menú (donde "x" es 0 ó 1).

Tipo es uno o más de los siguientes caracteres:

  n	no directorio
  r	archivo regular
  d	directorio
  l	enlace
  c	dispositivo tipo carácter
  b	dispositivo tipo bloque
  f	tubería (fifo)
  s	socket
  x	ejecutable
  t	marcado (tagged)

Por ejemplo 'rlf' significa archivo regular, enlace o
cola. El tipo 't' es un poco especial porque actúa sobre
el panel en vez de sobre un archivo. La condición '=t t'
es verdadera si existen archivos marcados en el panel
actual y falsa si no los hay.

Si la condición comienza con '=?' en vez de '=' se
mostrará un trazado de depuración mientras el valor de la
condición es calculado.

Las condiciones son calculadas de izquierda a derecha.
Esto significa que
	= f *.tar.gz | f *.tgz & t n
es calculado como
	( (f *.tar.gz) | (f *.tgz) ) & (t n)

He aquí un ejemplo de uso de condiciones:

= f *.tar.gz | f *.tgz & t n
L	Lista el contenido de un archivo tar comprimido
	gzip -cd %f | tar xvf -

Condiciones aditivas

Si la condición comienza con '+' (o '+?') en lugar de '='
(o '=?') es una condición aditiva. Si la condición es
verdadera la entrada de menú será incluida en el menú. Sin
embargo, si la condición es falsa, la entrada de menú no
será incluida en el menú.

Podemos combinar condiciones por defecto y aditivas
comenzando la condición con '+=' o '=+' (o '+=?' o '=+?'
si queremos depurar). Si nosotros queremos condiciones
diferentes, una para añadir y otra por defecto, una
entrada de menú con dos líneas de condición, una
comenzando con '+' y otra con '='.

Los comentarios empiezan con '#'. Las líneas adicionales
de comentarios deben empezar con '#', espacio o tab.[Options Menu]
Menú de Opciones

Midnight Commander tiene opciones que pueden ser activadas
o desactivadas a través de una serie de diálogos a los que
se accede desde este menú. Una opción está activada cuando
tiene delante un asterisco o una "x".

En ConfiguraciónConfiguration se pueden cambiar la mayoría de opciones
de Midnight Commander.

En PresentaciónLayout está un grupo de opciones que determinan
la apariencia de mc en la pantalla.

En ConfirmaciónConfirmation podemos especificar qué acciones requieren
una confirmación del usuario antes de ser realizadas.

En Juego de CaracteresDisplay bits podemos seleccionar qué caracteres
es capaz de mostrar nuestro terminal.

En Aprender TeclasLearn keys podemos verificar teclas que no
funcionan en algunos terminales y solucionarlo.

En Sistema de Archivos Virtual (VFS)Virtual FS podemos especificar
algunas opciones relacionadas con el VFS (Sistema de
Archivos Virtual).

Guardar ConfiguraciónSave Setup guarda los valores actuales de los
menús Izquierdo, Derecho y Opciones. También se guardan
algunos otros valores.[Configuration]
Configuración

Este diálogo presenta una serie de opciones divididas en
tres grupos: Opciones de los Paneles, Pausa Después de
Ejecutar y Otras Opciones.

Opciones de los paneles

Mostrar Archivos de Respaldo. Mostrar los archivos
terminados en tilde '~'. Por defecto, Midnight Commander
no los muestra (como la opción -B de ls de GNU).

Mostrar Archivos Ocultos. Mostrar los archivos que
comiencen con un punto (como ls -a).

Marcar y Avanzar. Hacer avanzar la barra de selección tras
marcar un archivo (con C-t o con la tecla Insertar).

Menús Desplegables. Mostrar el contenido de los menús
desplegables inmediatamente al presionar F9. Si está
desactivada sólo la barra de títulos de los menús está
visible, y será necesario abrir cada menú con las flechas
de movimiento o con las teclas de acceso rápido.

Mezclar Archivos y Directorios. Cuando esta opción está
habilitada, todos los archivos y directorios se muestran
mezclados. Si la opción está desactivada, los directorios
(y enlaces a directorios) aparecen al principio de la
lista, y el resto de archivos a continuación.

Recarga Rápida de Directorios. Hace que Midnight Commander
emplee una pequeña trampa al determinar si los contenidos
del directorio han cambiado. El truco consiste en recargar
el directorio sólo si el inodo del directorio ha cambiado.
Las recargas se producen si se crean o borrar archivos,
pero si lo que cambia es sólo el inodo de un archivo del
directorio (cambios en el tamaño, permisos, propietario,
etc.) la pantalla no se actualiza. En esos casos, si
tenemos la opción activada, será preciso forzar la recarga
de forma manual (con C-r).

Pausa Después de Ejecutar.

Después de ejecutar comandos, Midnight Commander puede
realizar una pausa, y darnos tiempo a examinar la salida
del comando. Hay tres posibles valores para esta variable:

Nunca. Significa que no queremos ver la salida de nuestros
comandos. Si estamos utilizando la consola Linux o FreeBSD
o un xterm, podremos ver la salida del comando pulsando
C-o.

Sólo en Terminales Tontas. Obtendremos el mensaje de pausa
sólo en terminales que no sean capaces de mostrar la
salida del último comando ejecutado (en realidad,
cualquier terminal que no sea un xterm o una consola de
Linux).

Siempre. El programa realizará siempre una pausa después
de ejecutar comandos.

Otras Opciones

Operación Detallada. Controla la visualización de detalles
durante las operaciones de Copiar, Mover y Borrar (i.e.,
muestra un cuadro de diálogo para cada operación). Si
tenemos un terminal lento, podríamos querer desactivar la
operación detallada. Se desactiva automáticamente si la
velocidad de nuestro terminal es menor de 9600 bps.

Calcular Totales. Hace que Midnight Commander calcule el
total de bytes y el número de archivos antes de iniciar
operaciones de Copiar, Mover y Borrar. Esto proporciona
una barra de progreso más precisa a costa de cierta
velocidad. Esta opción no tiene efecto si la Operación
Detallada no está seleccionada.

Patrones del shell. Por defecto, las funciones Selección,
Deselección y Filtro emplean expresiones regulares al
estilo del shell. Para realizar esto se realizan las
siguientes conversiones: '*' se cambia por '.*' (cero o
más caracteres); '?' por '.' (exactamente un carácter) y
'.' por un punto literal. Si la opción está desactivada,
entonces las expresiones regulares son las descritas en
ed(1).

Auto-Guardar Configuración. Si esta opción está activada,
cuando salimos de Midnight Commander las opciones
configurables de Midnight Commander se guardan en el
archivo ~/.mc/ini.

Auto Menús. Si está activada, el menú de usuario aparece
automáticamente al arrancar. Útil en menús construidos
para personas sin conocimientos de Unix.

Usar Editor Interno. Emplear el editor de archivos
interno. Si está desactivada, se editarán los archivos con
el editor especificado por la variable de entorno EDITOR y
si no se especifica ninguno, se usará vi. Véase la sección
sobre el editor de archivos internoInternal File Editor.

Usar Visor Interno. Emplear el visor de archivos interno.
Si la opción está desactivada, el paginador especificado
en la variable de entorno PAGER será el utilizado. Si no
se especifica ninguno, se usará el comando view. Véase la
sección sobre el visor de archivos internoInternal File Viewer.

Completar: Mostrar Todos. Por defecto, al completar
nombres en situaciones de ambigüedad, Midnight Commander
completa todo lo posible al pulsar M-Tab y produce un
pitido; al intentarlo por segunda vez se muestra una lista
con las posibilidades que han dado lugar a la ambigüedad.
Con esta opción, la lista aparece directamente tras pulsar
M-Tab por primera vez.

Hélice de actividad. Mostrar un guión rotatorio en la
esquina superior derecha a modo de indicador de progreso.

Navegación al Estilo Lynx. Cuando la selección es un
directorio y la línea de órdenes está vacía permite
cambiar a él con las flechas de movimiento. Esta opción
está inactiva por defecto.

Cd Sigue los Enlaces. Esta opción, si está seleccionada,
hace que Midnight Commander siga la secuencia de
directorios lógica al cambiar el directorio actual, tanto
en el panel como usando el comando cd. Éste es el
comportamiento por defecto de la shell bash. Sin esto,
Midnight Commander sigue la estructura real de
directorios, y cd .. nos trasladará al padre real del
directorio actual aunque hayamos entrado en ese directorio
a través de un enlace, y no al directorio donde se
encontraba el enlace.

Precauciones de Borrado. Dificulta el borrado accidental
de archivos. La opción por defecto en el diálogo de
confirmación de borrado se cambia a "No". Por defecto,
esta opción está desactivada.[Layout]
Presentación

La ventana de presentación nos da la posibilidad de
cambiar la presentación general de la pantalla. Podemos
configurar si son visibles la barra de menú, la línea de
órdenes, la línea de sugerencias o la barra de teclas de
Función. En la consola Linux o FreeBSD podemos especificar
cuántas líneas se muestran en la ventana de salida.

El resto del área de pantalla se utiliza para los dos
paneles de directorio. Podemos elegir si disponemos los
paneles vertical u horizontalmente. La división puede ser
simétrica o bien podemos indicar una división asimétrica.

Por defecto, todos los contenidos de los paneles se
muestran en el mismo color, pero se puede indicar que
permisos y tipos de archivos se resalten empleando coloresColors
diferentes. Si se activa el resaltado de permisos, las
partes de los campos de permisos del Modo de ListadoListing Mode...
aplicables al usuario actual de Midnight Commander serán
resaltados usando el color indicado por medio de la
palabra clave selected. Si se activa el resaltado de tipos
de archivos, los archivos aparecerán coloreados según su
tipo (i.e. directorios, archivos core, ejecutables,...).

Si la opción Mostrar Mini-Estado está activa se muestra,
en la parte inferior de cada panel, una línea con
información sobre el archivo seleccionado en cada momento.[Confirmation]
Confirmación

En este menú configuramos las opciones de confirmación de
eliminación de archivos, sobreescritura, ejecución
pulsando intro y salir del programa.[Display bits]
Bits de Visualización

Esta opción es utilizada para configurar el rango de
caracteres visibles en la pantalla. Esta selección puede
ser 7-bits si nuestro terminal/curses soporta sólo siete
bits de salida, ISO-8859-1 muestra todos los caracteres
del mapa ISO-8859-1 despliegue de 8 bit para aquellos
terminales que puedan los 8 bits en toda su extensión.[Learn keys]
Aprender teclas

Este diálogo nos permite comprobar si nuestras teclas
F1-F20, Inicio, Fin, etc. funcionan adecuadamente en
nuestro terminal. A menudo fallan, dado que muchas bases
de datos de terminales están mal.

Podemos movernos alrededor con la tecla Tab, con las
teclas de movimiento de vi ('h' izquierda, 'j' abajo, 'k'
arriba y 'l' derecha) y después de pulsar cualquier tecla
del cursor (esto las marcará con OK), entonces podremos
usar esa tecla también.

Para probarlas basta con pulsar cada una de ellas. Tan
pronto como pulsamos una tecla y ésta funciona
adecuadamente, OK debería aparecer junto al nombre de la
susodicha tecla. Una vez que una tecla es marcada con OK
empieza a funcionar con normalidad, p.e. F1 la primera vez
comprobará que F1 funciona perfectamente, pero a partir de
ese momento mostrará la ayuda. Esto mismo es aplicable a
las teclas del cursor. La tecla tab debería funcionar
siempre.

Si algunas teclas no funcionan adecuadamente, entonces no
veremos el OK tras el nombre de la tecla después de
haberla pulsado. Podemos entonces intentar solucionarlo.
Haremos esto pulsando el botón de esa tecla (con el ratón
o usando Tab e Intro). Entonces un mensaje rojo aparecerá
y se nos pedirá que pulsemos la tecla en cuestión. Si
deseamos abortar el proceso, bastará con pulsar Esc y
esperar hasta que el mensaje desaparezca. Si no,
pulsaremos la tecla que nos pide y esperaremos hasta que
el diálogo desaparezca.

Cuando acabemos con todas las teclas, podríamos Guardar
nuestras teclas en nuestro archivo ~/.mc/ini dentro de la
sección [terminal:TERM] (donde TERM es el nombre de
nuestro terminal actual) o descartarlas. Si todas nuestras
teclas funcionan correctamente y no debemos corregir
ninguna, entonces (lógico) no se grabará.[Virtual FS]
Sistema de Archivos Virtual (VFS)

Este diálogo permite ajustar opciones del Sistema de
Archivos Virtual (VFS)Virtual File System.

Midnight Commander guarda en memoria o en disco
información de algunos de los sistemas de archivos
virtuales con el fin de acelerar el acceso a sus archivos.
Ejemplo de esto son los listados descargados desde
servidores FTP o los archivos temporales descomprimidos
creados para acceder rápidamente a los contenidos de
archivos tipo tar comprimidos.

Esas informaciones se conservan para permitirnos navegar,
salir y volver a entrar rápidamente en los
correspondientes sistemas de archivos virtuales. Al cabo
de un cierto tiempo sin usarlos deben ser liberados y
recuperar los recursos utilizados. Por defecto ese tiempo
es de un minuto, pero se puede configurar por el usuario.

También podemos adelantar la liberación de los VFS desde
el diálogo de control de Directorios virtuales (VFS).

El Sistema de Archivos FTP (FTPfs)FTP File System permite navegar por
los directorios de servidores FTP remotos. Admite diversas
opciones.

Contraseña de FTP anónimo es la contraseña a utilizar en
conexiones en modo anónimo, esto es, empleando el nombre
de usuario "anonymous". Algunos sitios exigen que ésta sea
una dirección de correo electrónico válida, pero tampoco
es conveniente dar nuestra dirección real a desconocidos
para protegernos de los envíos de correo masivo.

FTPfs conserva en caché los listados de los directorios
consultados. La duración de la caché es el valor indicado
tras Descartar el caché FTPfs. Un valor pequeño ralentiza
el proceso porque cualquier pequeña operación iría siempre
acompañada de una conexión con el servidor FTP.

Se puede configurar un sistema proxy para FTP, aunque los
cortafuegos modernos son transparentes (al menos para FTP
pasivo, ver más abajo) y está opción es generalmente
innecesaria.

Si la opción Usar siempre proxy no está activa, aún se
puede emplear el proxy en casos concretos. Véanse los
ejemplos en la sección Sistema de Archivos FTP (FTPfs)FTP File System.

Si la opción Usar siempre proxy está puesta, el programa
asume que cualquier nombre de máquina sin puntos es
accesible directamente y también consulta el archivo
/usr/share/mc.no_proxy en busca de nombres de máquinas
locales (o dominios completos si el nombre empieza con un
punto). En todos los demás casos se usará siempre el proxy
de FTP indicado arriba.

Se puede usar el archivo ~/.netrc, que contiene
información de usuarios y contraseñas para determinados
servidores FTP. Para conocer el formato de los archivos
.netrc véase netrc (5).

Usar FTP pasivo habilita el modo de tranferencia FTP
pasivo (la conexión para transferencia de datos es
iniciada por la máquina cliente, no por el servidor). Esta
opción es la recomendada, y de hecho está activada por
defecto. Si se desactiva, la conexión la inicia el
servidor, y puede ser impedida por algún cortafuegos.

[Save Setup]
Guardar Configuración

Al arrancar Midnight Commander se carga la información de
inicio del archivo ~/.mc/ini. Si éste no existe, se
cargará la información del archivo de configuración
genérico del sistema, /usr/share/mc/mc.ini. Si el archivo
de configuración genérico del sistema no existe, MC
utiliza la configuración por defecto.

El comando Guardar Configuración crea el archivo ~/.mc/ini
guardando la configuración actual de los menús Izquierdo,
DerechoLeft and Right Menus y OpcionesOptions Menu.

Si se activa la opción Auto-guarda configuración, MC
guardará siempre la configuración actual al salir.

Existen también configuraciones que no pueden ser
cambiadas desde los menús. Para cambiarlas hay que editar
manualmente el archivo de configuración. Para más
información, véase la sección sobre Ajustes EspecialesSpecial Settings.

[Executing operating system commands]
Ejecutando Órdenes del Sistema Operativo

Podemos ejecutar comandos tecleando en la línea de órdenes
de Midnight Commander, o seleccionando el programa que
queremos ejecutar en alguno de los paneles y pulsando
Intro.

Si pulsamos Intro sobre un archivo que no es ejecutable,
Midnight Commander compara la extensión del archivo
seleccionado con las extensiones recogidas en el Archivo
de ExtensionesExtension File Edit. Si se produce una coincidencia se
ejecutará el código asociado con esa extensión. Tendrá
lugar una expansiónMacro Substitution muy simple antes de ejecutar el
comando.[The cd internal command]
Comando cd Interno

El comando cd es interpretado directamente por Midnight
Commander, en vez de pasarlo al interprete de comandos
para su ejecución. Por ello puede que no todas las
posibilidades de expansión y sustitución de macro que hace
nuestro shell estén disponibles, pero sí algunas de ellas:

Sustitución de tilde. La tilde (~) será sustituida por
nuestro directorio de inicio. Si añadimos un nombre de
usuario tras la tilde, entonces será sustituido por el
directorio de entrada al sistema del usuario especificado.

Por ejemplo, ~coco sería el directorio de un supuesto
usuario denominado "coco", mientras que ~/coco es el
directorio coco dentro de nuestro propio directorio de
inicio.

Directorio anterior. Podemos volver al directorio donde
estábamos anteriormente empleando el nombre de directorio
especial '-' del siguiente modo: cd -

Directorios en CDPATH. Si el directorio especificado al
comando cd no está en el directorio actual, entonces
Midnight Commander utiliza el valor de la variable de
entorno CDPATH para buscar el directorio en cualquiera de
los directorios enumerados.

Por ejemplo, podríamos asignar a nuestra variable CDPATH
el valor ~/src:/usr/src, lo que nos permitiría cambiar de
directorio a cualquiera de los directorios dentro de ~/src
y /usr/src, desde cualquier lugar del sistema de archivos,
usando sólo su nombre relativo (por ejemplo cd linux
podría llevarnos a /usr/src/linux).[Macro Substitution]
Sustitución de Macro

Cuando se accede al menú de usuarioMenu File Edit, o se ejecuta un
comando dependiente de extensiónExtension File Edit, o se ejecuta un
comando desde la línea de entrada de comandos, se realiza
una simple sustitución de macro.

Las macros son:

"%f"

        Archivo actual.

"%d"

        Nombre del directorio actual.

"%F"

        Archivo actual en el panel inactivo.

"%D"

        Directorio del panel inactivo.

"%t"

        Archivos actualmente marcados.

"%T"

        Archivos marcados en el panel inactivo.

"%u" y "%U"

        Similar a las macros %t y %T, salvo que los
        archivos quedan desmarcados. Sólo se puede
        emplear esta macro una vez por cada entrada del
        archivo de menú o archivo de extensiones, puesto
        que para la siguiente vez no quedaría ningún
        archivo marcado.

"%s" y "%S"

        Archivos seleccionados: Los archivos marcados si
        los hay y si no el archivo actual.

"%cd"

        Ésta es una macro especial usada para cambiar del
        directorio actual al directorio especificado
        frente a él. Esto se utiliza principalmente como
        interfaz con el Sistema de Archivos VirtualVirtual File System.

"%view"

        Esta macro es usada para invocar al visor
        interno. Puede ser utilizada en solitario, o bien
        con argumentos. Si pasamos algún argumento a esta
        macro, deberá ser entre paréntesis.

        Los argumentos son: ascii para forzar al visor a
        modo ascii; hex para forzar al visor a modo
        hexadecimal; nroff para indicar al visor que debe
        interpretar las secuencias de negrita y subrayado
        de nroff; unformated para indicar al visor que no
        interprete los comandos nroff referentes a texto
        resaltado o subrayado.

"%%"

        El carácter %

"%{cualquier texto}"

        Pregunta sobre la sustitución. Un cuadro de
        entrada es mostrado y el texto dentro de las
        llaves se usa como mensaje. La macro es
        sustituida por el texto tecleado por el usuario.
        El usuario puede pulsar ESC o F10 para cancelar.
        Esta macro no funciona aún sobre la línea de
        órdenes.[The subshell support]
Soporte de Subshell

El soporte del subshell es una opción de tiempo de
compilación, que funciona con los shells: bash, tcsh y
zsh.

Cuando el código del subshell es activado Midnight
Commander engendrará una copia de nuestro shell (la
definida en la variable SHELL y si no está definida, el
que aparece en el archivo /etc/passwd) y lo ejecuta en un
pseudoterminal, en lugar de invocar un nuevo shell cada
vez que ejecutamos un comando, el comando será pasado al
subshell como si lo hubiésemos escrito. Esto además
permite cambiar las variables de entorno, usaremos las
funciones del shell y los alias definidos que serán
válidos hasta salir de Midnight Commander.

Si estamos usando bash podremos especificar comandos de
arranque para el subshell en nuestro archivo ~/.mc/bashrc
y mapas de teclado especiales en el archivo ~/.mc/inputrc.
Los usuarios de tcsh podrán especificar los comandos de
arranque en el archivo ~/.mc/tcshrc.

Cuando utilizamos el código del subshell, podemos
suspender aplicaciones en cualquier momento con la
secuencia C-o y volver a Midnight Commander, si
interrumpimos una aplicación, no podremos ejecutar otros
comandos externos hasta que quitemos la aplicación que
hemos interrumpido.

Una característica extra añadida de uso del subshell es
que el prompt mostrado por Midnight Commander es el mismo
que estamos usando en nuestro shell.

La sección OPCIONES tiene más información sobre cómo
controlar el código del subshell.[Chmod]
Cambiar Permisos

Cambiar Permisos se usa para cambiar los bits de permisos
en un grupo de archivos y directorios. Puede ser invocado
con la combinación de teclas C-x c.

La ventana de Cambiar Permisos tiene dos partes - Permisos
y Archivo

En la sección Archivo se muestran el nombre del archivo o
directorio y sus permisos en formato numérico octal, así
como su propietario y grupo.

En la sección de Permisos hay un grupo de casillas de
selección que corresponden a los posibles permisos del
archivo. Conforme los cambiamos podemos ver cómo el valor
octal va cambiando en la sección Archivo.

Para desplazarse entre las casillas y botones de la
ventana podemos usar las teclas del cursor o la tecla de
tabulación. Para marcar o desmarcar casillas y para pulsar
los botones usaremos la barra espaciadora. Podemos usar
los atajos de teclado (las letras destacadas) para
accionar directamente los elementos.

Para aceptar y aplicar los permisos, usaremos la tecla
Intro.

Si se trata de un grupo de archivos o directorios, podemos
cambiar parte de los permisos marcándolos (las marcas son
los asteriscos a la izquierda de las casillas) y pulsando
el botón [* Poner] o [* Quitar] para indicar la acción
deseada. Los permisos no marcados conservan, en este caso,
los valores previos.

Podemos también fijar todos los permisos iguales en todos
los archivos con el botón [Todos] o sólo los permisos
marcados con el botón [* Todos]. En estos casos las
casillas indican el estado en que queda cada permiso,
igual que para archivos individuales.

[Todos] actúa sobre todos los permisos de todos los
archivos

[* Todos] actúa sólo sobre los atributos marcados de los
archivos

[* Poner] activa los permisos marcados en los archivos
seleccionados

[* Quitar] desactiva los permisos marcados en los archivos
seleccionados

[Aplicar] actúa sobre todos los permisos de cada archivo,
uno a uno

[Cancelar] cancela Cambiar Permisos[Chown]
Cambiar Dueño

Cambiar Dueño permite cambiar el propietario y/o grupo de
un archivo. La tecla rápida para este comando es C-x o.[Advanced Chown]
Cambiar Dueño y Permisos

Cambiar Dueño y Permisos combina Cambiar DueñoChown y Cambiar
PermisosChmod en una única ventana. Se puede así cambiar los
permisos, propietario y grupo del archivo de una sola vez.[File Operations]
Operaciones con Archivos

Cuando copiamos, movemos o borramos archivos, Midnight
Commander muestra el diálogo de operaciones con archivos.
En él aparecen los archivos que se estén procesando y
hasta tres barras de progreso. La barra de archivo indica
qué parte del archivo actual va siendo copiada, la barra
de contador indica cuántos de los archivos marcados han
sido completados y la barra de bytes nos dice qué parte
del tamaño total de archivos marcados ha sido procesado
hasta el momento. Si la operación detallada está
desactivada no se muestran las barras de archivo y bytes.

En la parte inferior hay dos botones. Pulsando el botón
Saltar se ignorará el resto del archivo actual. Pulsando
el botón Abortar se detendrá la operación y se ignora el
resto de archivos.

Hay otros tres diálogos que pueden aparecer durante
operaciones de archivos.

El diálogo de error informa sobre una condición de error y
tiene tres posibilidades. Normalmente seleccionaremos el
botón Saltar para evitar el archivo o Abortar para detener
la operación. También podemos seleccionar el botón
Reintentar si hemos corregido el problema desde otro
terminal.

El diálogo Reemplazar aparece cuando intentamos copiar o
mover un archivo sobre otro ya existente. El mensaje
muestra fechas y tamaños de ambos archivos. Pulsaremos el
botón Sí para sobreescribir el archivo, el botón No para
saltarlo, el botón Todos para sobreescribir todos los
archivos, Ninguno para no sobreescribir en ningún caso y
Actualizar para sobreescribir si el archivo origen es
posterior al archivo objeto. Podemos abortar toda la
operación pulsando el botón Abortar.

El diálogo de eliminación recursiva aparece cuando
intentamos borrar un directorio no vacío. Pulsaremos Sí
para borrar el directorio recursivamente, No para saltar
el directorio, Todo para borrar recursivamente todos los
directorios marcados no vacíos y Ninguno para saltarlos
todos. Podemos abortar toda la operación pulsando el botón
Abortar. Si seleccionamos el botón Sí o Todo se nos pedirá
confirmación. Diremos "sí" sólo si estamos realmente
seguros de que queremos una eliminación recursiva.

Si hemos marcado archivos y realizamos una operación sobre
ellos, sólo los archivos sobre los que la operación fue
exitosa son desmarcados. Los archivos saltados y aquellos
en los que la operación falló permanecen marcados.[Mask Copy/Rename]
Copiar/Renombrar con Máscara

Las operaciones de copiar/mover permiten transformar los
nombres de los archivos de manera sencilla. Para ello, hay
que procurar una máscara correcta para el origen y
normalmente en la terminación del destino algunos
caracteres comodín. Todos los archivos que concuerden con
la máscara origen son copiados/renombrados según la
máscara destino. Si hay archivos marcados, sólo aquellos
que encajen con la máscara de origen serán renombrados.

Hay otras opción que podemos seleccionar:

Seguir Enlaces indica si los enlaces simbólicos o físicos
en el directorio origen (y recursivamente en sus
subdirectorios) producen nuevos enlaces en el directorio
destino o si queremos copiar su contenido.

Copiar Recursivamente indica qué hacer si en el directorio
destino existe ya un directorio con el mismo nombre que el
archivo/directorio que está siendo copiado. La acción por
defecto es copiar su contenido sobre ese directorio.
Habilitando esto podemos copiar el directorio de origen
dentro de ese directorio. Quizás un ejemplo pueda ayudar:

Queremos copiar el contenido de un directorio denominado
coco a /blas donde ya existe un directorio /blas/coco. Por
defecto, mc copiaría el contenido en /blas/coco, pero con
esta opción se copiaría como /blas/coco/coco.

Preservar Atributos indica que se deben conservar los
permisos originales de los archivos, marcas temporales y
si somos superusuario también el propietario y grupo
originales. Si esta opción no está activa se aplica el
valor actual de umask.

"Usando Patrones Shell activado"

Usando Patrones Shell nos permite usar los caracteres
comodín '*' y '?' en la máscara de origen. Funcionará
igual que en la línea de órdenes. En la máscara destino,
sólo están permitidos los comodines '*' y '\<número>'. El
primer '*' en la máscara destino corresponde al primer
grupo del comodín en la máscara de origen, el segundo '*'
al segundo grupo, etcétera. El comodín '\1' corresponde al
primer grupo en la máscara de origen, el comodín '\2' al
segundo y así sucesivamente hasta '\9'. El comodín '\0' es
el nombre completo del archivo fuente.

Dos ejemplos:

Si la máscara de origen es "*.tar.gz", el destino es
"/blas/*.tgz" y el archivo a copiar es "coco.tar.gz", la
copia se hará como "coco.tgz" en "/blas".

Supongamos que queremos intercambiar el nombre y la
extensión de modo que "archivo.c" se convierta en
"c.archivo". La máscara origen será "*.*" y la de destino
"\2.\1".

"Usando Patrones Shell desactivado"

Cuando la opción de Patrones Shell está desactivada MC no
realiza una agrupación automática. Deberemos usar
expresiones '\(...\)' en la máscara origen para
especificar el significado de los comodines en la máscara
destino. Esto es más flexible pero también necesita más
escritura. Por lo demás, las máscaras destino son
similares al caso de Patrones Shell activos.

Dos ejemplos:

Si la máscara de origen es "^\(.*\)\.tar\.gz$", el destino
es "/blas/*.tgz" y el archivo a ser copiado es
"coco.tar.gz", la copia será "/blas/coco.tgz".

Si queremos intercambiar el nombre y la extensión para que
"archivo.c" sea "c.archivo", la máscara de origen puede
ser "^\(.*\)\.\(.*\)$" y la de destino "\2.\1".

"Capitalización"

Podemos hacer cambios entre mayúsculas y minúsculas en los
nombres de archivos. Si usamos '\u' o '\l' en la máscara
destino, el siguiente carácter será convertido a
mayúsculas o minúsculas respectivamente.

Si usamos '\U' o '\L' en la máscara destino, los
siguientes caracteres serán convertidos a mayúsculas o
minúsculas respectivamente hasta encontrar '\E' o un
segundo '\U' o '\L' o el fin del nombre del archivo.

'\u' y '\l' tienen prioridad sobre '\U' y '\L'.

Por ejemplo, si la máscara fuente es '*' (con Patrones
Shell activo) o '^\(.*\)$' (Patrones Shell desactivado) y
la máscara destino es '\L\u*' los nombres de archivos
serán convertidos para que tengan su inicial en mayúscula
y el resto del nombre en minúsculas.

También podemos usar '\' como carácter de escape evitando
la interpretación de todos estos caracteres especiales.
Por ejemplo, '\\' es una contrabarra y '\*' es un
asterisco.[Internal File Viewer]
Visor de Archivos Interno

El visor de archivos interno ofrece dos modos de
presentación: ASCII y hexadecimal. Para alternar entre
ambos modos, se emplea la tecla F4.

El visor intenta usar el mejor método disponible en el
sistema, según el tipo de archivo, para mostrar
información. Los archivos comprimidos se descomprimen
automáticamente si los programas correspondientes (GNU
gzip ó bzip2) están instalados en el sistema. El propio
visor es capaz de interpretar ciertas secuencias de
caracteres que se emplean para activar los atributos de
negrita y subrayado, mejorando la presentación de los
archivos.

En modo hexadecimal, la función de búsqueda admite texto
entre comillas o valores numéricos. El texto
entrecomillado se busca tal cual (retirando las comillas)
y cada número se corresponde a un byte. Unos y otros se
pueden entremezclar como en:

"Cadena" -1 0xBB 012 "otro texto"

Nótese que 012 es un número octal y -1 se convierte en
0xFF.

Algunos detalles internos del visualizador: En sistemas
con acceso a la llamada del sistema mmap(2), el programa
mapea el archivo en vez de cargarlo; si el sistema no
provee de la llamada al sistema mmap(2) o el archivo
realiza una acción que necesita de un filtro, entonces el
visor usará sus cachés de crecimiento, cargando sólo las
partes del archivo a las que actualmente estamos
accediendo (esto incluye a los archivos comprimidos).

He aquí una lista de las acciones asociadas a cada tecla
que Midnight Commander gestiona en el visor interno de
archivos.

F1 Invoca el visor de ayuda de hipertexto interno.

F2 Cambia el modo de ajuste de líneas en pantalla.

N. del T.- Envuelta (Ajustada), se muestra toda la
información de la línea en la pantalla, de modo que si
ésta ocupa más del ancho de la pantalla aparece como si
fuese otra línea aparte o bien desenvuelta (desajustada),
truncando el contenido de la línea que sobresale de la
pantalla. Este contenido puede ser consultado utilizando
las teclas del cursor.

F4 Cambia entre el modo hexadecimal y el Ascii.

F5 Ir a la línea. Nos pedirá el número de línea en el que
deseamos posicionarnos y mostrará el archivo a partir de
esa línea.

F6, /. Búsqueda de expresión regular desde la posición
actual hacia adelante.

?, Búsqueda de expresión regular desde la posición actual
hacia atrás.

F7 Búsqueda normal/ búsqueda en modo hexadecimal.

C-s. Comienza una búsqueda normal si no existe una
expresión de búsqueda previa si no busca la próxima
coincidencia.

C-r. Comienza una búsqueda hacia atrás si no había
expresión de búsqueda anterior si no busca la próxima
coincidencia.

n. Buscar la próxima coincidencia.

F8 Intercambia entre el modo crudo y procesado: esto
mostrará el archivo como se encuentra en disco o si se ha
especificado un filtro de visualización en el archivo
mc.ext, entonces la salida filtrada. El modo actual es
siempre el contrario al mostrado en la etiqueta del botón,
en tanto que el botón muestra el modo en el que entraremos
con la pulsación de esa tecla.

F9 Alterna entre la visualización con y sin formato: en el
modo con formato se interpretan algunas secuencias de
caracteres para mostrar texto en negrita y subrayado con
diferentes colores. Como en el caso anterior, la etiqueta
del botón muestra el estado contrario al actual.

F10, Esc. Sale del visor interno.

Av pág, espacio, C-v. Avanza una página hacia abajo.

Re pág, M-v, C-b, Retroespacio. Retrocede una página hacia
arriba.

Cursor Abajo Desplaza el texto una línea hacia arriba,
mostrando en la línea inferior de la pantalla una nueva
línea que antes quedaba oculta.

Cursor Arriba Desplaza una línea hacia abajo.

C-l Redibuja el contenido de la pantalla.

! Engendra un nuevo shell en el directorio de trabajo
actual.

"[n] m" Coloca la marca n.

"[n] r" Salta hasta la marca n.

C-f Salta al archivo siguiente.

C-b Ídem al archivo anterior.

M-r Intercambia entre los diferentes modos de regla:
desactivado, arriba, abajo.

Es posible adiestrar al visor de archivos sobre cómo
mostrar un archivo, mírese la sección Editar Archivo de
ExtensionesExtension File Edit.[Internal File Editor]
Editor de Archivos Interno

El editor de archivos interno es un editor a pantalla
completa de avanzadas prestaciones. Puede editar archivos
de hasta 64 MB y también permite modificar archivos
binarios. Se inicia pulsando F4 supuesto que la variable
use_internal_edit esté presente en el archivo de
inicialización.

Las características soportadas actualmente son: copia,
desplazamiento, borrado, corte, y pegado de bloques;
deshacer paso a paso; menús desplegables; inserción de
archivos; definición de macros; buscar y reemplazar usando
expresiones regulares (y su propio buscar y reemplazar
basado en formatos de scanf/printf); selección de texto
con mayúsculas-cursor (si el terminal lo soporta);
alternancia insertar-sobreescribir; plegado de líneas;
sangrado automático; tamaño de tabulación configurable;
realce de sintaxis para varios tipos de archivos; y la
opción de pasar bloques de texto por filtros externos como
indent o ispell.

El editor es muy fácil de usar y no requiere aprendizaje
alguno. Para conocer las teclas asignadas a cada función,
basta consultar los menús correspondientes. Además, las
teclas de desplazamiento con la tecla de mayúsculas
seleccionan texto. Se puede seleccionar con el ratón,
aunque podemos recuperar su funcionamiento habitual en
terminales (copiar y pegar) manteniendo pulsada la tecla
mayúsculas. Ctrl-Ins copia al archivo cooledit.clip y
Mayúsculas-Ins pega desde cooledit.clip. Mayúsculas-Supr
corta y copia en cooledit.clip, y Ctrl-Supr elimina el
texto resaltado. La tecla Intro produce un salto de línea
con sangrado automático opcional.

Para definir una macro, pulsar Ctrl-R y entonces
teclearemos las secuencias de teclas que deseamos sean
ejecutadas. Pulsaremos Ctrl-R de nuevo al finalizar.
Podemos asignar la macro a la tecla que queramos pulsando
sobre ella. La macro será ejecutada cuando pulsemos Ctrl-A
seguido de la tecla asignada. También será ejecutada si
pulsamos Meta (Alt), Ctrl, o Escape y la tecla asignada,
siempre y cuando la tecla no sea usada por ninguna otra
función. Una vez definida, los comandos de macro irán al
archivo cedit/cooledit.macros en nuestro directorio de
inicio. Podemos eliminar una macro borrando la línea
adecuada en este archivo.

F19 formateará el bloque seleccionado (sea texto, código C
o C++ u otro). Esto está controlado por el archivo
/usr/share/mc/edit.indent.rc que se copia la primera vez
que se usa en .mc/cedit/edit.indent.rc en el directorio
personal.

Podemos usar la búsqueda scanf y reemplazar para buscar y
cambiar una cierta cadena en formato C. Se pueden
consultar las páginas del manual de sscanf y sprintf para
saber qué es una cadena de formato y cómo funciona. Veamos
un ejemplo: supongamos que queremos cambiar todas las
apariciones de un paréntesis abierto, tres números
separados por comas, y un paréntesis cerrado, con la
palabra Melones_De_Pozo-Estrecho, el tercer número, la
palabra Tomates_De_Mazarrón y el segundo número.
Rellenaremos el diálogo Reemplazar como sigue:

 Teclee el texto a buscar:
  (%d,%d,%d)
 Teclee el cambio a realizar:
  Melones_De_Pozo-Estrecho %d Tomates_De_Mazarrón %d
 Teclee el orden de los argumentos:
  3,2

La última línea indica que el tercer y el segundo número
deben ser usados en primer y segundo lugar
respectivamente.

Es conveniente usar esta característica con "Confirmar
cambios" marcado, porque se pueden producir coincidencias
que no correspondan exactamente con lo deseado. Scanf
también trata el espacio en blanco como si fuese elástico.
El formato de scanf %[ resulta muy útil para rastrear
cadenas, y el espacio en blanco.

El editor también visualiza caracteres no estadounidenses
(160+). Al editar archivos binarios, debemos configurar
los bits de pantalla a 7 bits en el menú de opciones para
mantener el espaciado saneado.[Completion]
Terminación

Permite a Midnight Commander escribir por nosotros.

Intenta completar el texto escrito antes de la posición
actual. MC intenta la terminación tratando el texto como
si fuera una variable (si el texto comienza con $ ),
nombre de usuario (si el texto empieza por ~ ), nombre de
máquina (si el texto comienza con @ ) o un comando (si
estamos en la línea de órdenes en una posición donde
podríamos escribir un comando; las terminaciones posibles
entonces incluyen las palabras reservadas del shell así
como comandos internos del shell) en ese orden. Si nada de
lo anterior es aplicable, se intenta la terminación con
nombres de archivo.

La terminación de nombres de archivo, usuario y máquina
funciona en todas las líneas de entrada; la terminación de
comandos es específica de la línea de órdenes. Si la
terminación es ambigua (hay varias posibilidades
diferentes), MC pita, y la acción siguiente depende de la
opción Completar: Mostrar Todos en el diálogo de
ConfiguraciónConfiguration. Si está activada, se despliega
inmediatamente junto a la posición actual una lista con
todas las posibilidades donde se puede seleccionar con las
flechas de movimiento e Intro la entrada correcta. También
podemos seguir escribiendo caracteres con lo que la línea
se sigue completando tanto como sea posible y
simultáneamente la primera entrada coincidente de la lista
se va resaltando. Si volvemos a pulsar M-Tab, sólo las
coincidencias permanecen en la lista. Tan pronto como no
haya ambigüedad, la lista desaparece; también podemos
quitarla con las teclas de cancelación Esc, F10 y las
teclas de movimiento a izquierda y derecha. Si Completar:
Mostrar TodosConfiguration está desactivado, la lista aparece cuando
pulsamos M-Tab por segunda vez; con la primera MC sólo
emite un pitido.[Virtual File System]
Sistemas de Archivos Virtuales (VFS)

Midnight Commander dispone de una capa de código de acceso
al sistema de archivos; esta capa se denomina Sistema de
Archivos Virtual (VFS). El Sistema de Archivos Virtual
permite a Midnight Commander manipular archivos no
ubicados en el sistema de archivos Unix.

Midnight Commander incluye actualmente varios Sistemas de
Archivos Virtuales: el sistema de archivos local,
utilizado para acceder al sistema de archivos Unix
habitual; tarfs para manipular archivos empaquetados con
el comando tar y acaso comprimidos; undelfs para recuperar
archivos borrados en sistemas de archivos de tipo ext2
(sistema de archivos habitual en Linux); FTPfs para
manipular archivos en sistemas remotos a través de FTP;
FISH para manipular archivos a través de conexiones a
shell como rsh o ssh y finalmente MCfs (Midnight Commander
file system), un sistema de archivos para red. Si el
programa se compiló incluyendo SMBfs se pueden manipular
archivos en sistemas remotos empleando el protocolo SMB
(CIFS).

Se facilita también un sistema de archivos genérico extfs
(EXternal virtual File System) para extender con facilidad
las posibilidades de VFS empleando guiones y programas
externos.

El código VFS interpretará todos los nombres de ruta
usados y los dirigirá al sistema de archivos correcto. El
formato usado para cada uno de los sistemas de archivos se
describe más adelante en su propia sección.[Tar File System]
Sistema de archivos Tar (tarfs)

El sistema de archivos tar y los archivos tar comprimidos
pueden consultarse usando el comando chdir. Para mostrar
en el panel el contenido de un archivo tar, cambiamos de
directorio empleando la siguiente sintaxis:

/archivo.tar#utar/[directorio-dentro-tar]

El archivo mc.ext también ofrece un atajo para los
archivos tar, esto quiere decir que normalmente basta con
apuntar a un archivo tar y pulsar Intro para entrar en el
archivo tar. Véase la sección Edición del Archivo de
ExtensionesExtension File Edit para obtener más detalles sobre cómo hacer
esto.

Ejemplos:

    mc-3.0.tar.gz#utar/mc-3.0/vfs
    /ftp/GCC/gcc-2.7.0.tar#utar

En este último se indica la ruta completa hasta el archivo
tar.[FTP File System]
Sistema de archivos FTP (FTPfs)

FTPfs permite manipular archivos en máquinas remotas. Para
utilizarlo se puede emplear la opción de menú Conexión por
FTP o simplemente emplear la orden cd como cuando
cambiamos habitualmente de directorio, pero indicando como
ruta:

/#ftp:[!][usuario[:clave]@]maquina[:puerto][dir-remoto]

Los elementos usuario, puerto y directorio-remoto son
opcionales. Si especificamos el elemento usuario, entonces
Midnight Commander intentará conectarse con la máquina
remota como ese usuario, y si no, establecerá una conexión
en modo anónimo o con el nombre de usuario indicado en el
archivo ~/.netrc. El elemento clave también es opcional, y
si está presente, se emplea como contraseña de acceso.
Esta forma de colocar la contraseña como parte del nombre
del directorio virtual no es muy recomendable porque
eventualmente puede aparecer en pantalla y guardarse en el
histórico de directorios.

Si es necesario utilizar un proxy de FTP, se añade un
símbolo de exclamación ! delante del nombre de la máquina.

Ejemplos:

    /#ftp:ftp.nuclecu.unam.mx/linux/local
    /#ftp:tsx-11.mit.edu/pub/linux/packages
    /#ftp:!detras.barrera.edu/pub
    /#ftp:guest@pcremoto.com:40/pub
    /#ftp:miguel:xxx@servidor/pub
    /#ftp:ftp.um.es/pub

La opciones de FTPfs se encuentran entre las opciones de
configuración del Sistema de Archivos Virtual (VFS)Virtual FS.[FIle transfer over SHell filesystem]
Sistema de archivos de envío Archivos por SHell (FISH)

El FISH es un sistema de archivos por red que permite
manipular archivos en una máquina remota como si
estuvieran almacenados localmente. Para ello es preciso
que el sistema remoto este ejecutando el servidor FISH o
que la shell sea de tipo bash.

Para conectar con la máquina remota basta cambiar de
directorio a un directorio virtual cuyo nombre sea de la
forma:

/#sh:[usuario@]maquina[:opciones]/[directorio-remoto]

Los elementos usuario, opciones y directorio-remoto son
opcionales. Si se especifica el elemento usuario Midnight
Commander intentará entrar en la máquina remota como ese
usuario, y si no usará nuestro nombre.

Como opciones se puede poner 'C' para usar compresión y
'rsh' para utilizar una conexión rsh en vez de ssh. Si se
indica el directorio-remoto, se buscará éste como primer
directorio al conectar con la máquina remota.

Ejemplos:

    /#sh:solorsh.es:r/linux/local
    /#sh:pepe@quiero.comprension.edu:C/privado
    /#sh:pepe@sincomprimir.ssh.edu/privado
[Network File System]
Sistema de archivos de Red

El sistema de archivos de Midnight Commander es un sistema
de archivos de red básico que nos permite manipular
archivos en una máquina remota como si estuviesen
accesibles localmente. Para utilizar esto, la máquina
remota debe estar ejecutando el programa servidor
mcserv(8).

Para conectar a una máquina remota, sólo necesitamos hacer
un chdir a un directorio especial cuyo nombre sigue el
siguiente formato:

/#mc:[usuario@]máquina[:puerto][directorio-remoto]

Los elementos usuario, puerto y directorio-remoto son
opcionales. Si especificamos el elemento usuario entonces
Midnight Commander intentará acceder a la máquina como ese
usuario, si no, usará nuestro login.

El elemento puerto es necesario cuando el servidor remoto
se ejecuta en un puerto especial (véase la página del
manual de mcserv(8) para más información acerca de
puertos); finalmente, si el elemento directorio-remoto
está presente, nuestro directorio actual en la máquina
remota será éste.

Ejemplos:

    /#mc:ftp.nuclecu.unam.mx/linux/local
    /#mc:pepe@foo.edu:11321/privado
[SMB File System]
Sistema de archivos SMB

El SMBfs permite manipular archivos en máquinas remotas
con el protocolo denominado SMB (o CIFS). Esto incluye
Windows Trabajo en Grupo, Windows 9x/ME/XP, Windows NT,
Windows 2000 y Samba. Para comenzar a usarlo, se puede
emplear la "Conexión por SMB..." (accesible desde la barra
de menús) o bien cambiar de directorio a un directorio
virtual cuyo nombre sea de la forma:

/#smb:[usuario@]maquina[/recurso][/directorio-remoto]

Los elementos usuario, recurso y directorio-remoto son
opcionales. El usuario, dominio y contraseña se pueden
especificar en un cuadro de diálogo.

Ejemplos:

    /#smb:maquina/Compartido
    /#smb:otramaquina
    /#smb:invitado@maquina/publico/leyes
[Undelete File System]
Sistema de archivos de Recuperación

En sistemas Linux, si el programa de configuración nos
preguntó si queríamos usar las facilidades de recuperación
de archivos de ext2fs, tendremos el sistema de archivos
recuperables accesible. La recuperación de archivos
borrados está disponible sólo en los sistemas de archivos
ext2. El sistema de archivos recuperable es sólo un
interface de la librería ext2fs con: restaurar todos los
archivos borrados en un ext2fs y proporciona la extracción
selectiva de archivos en una partición regular.

Para usar este sistema de archivos, tendremos que hacer un
chdir a un nombre de archivo especial formado por el
prefijo "/#undel" y el nombre de archivo donde se
encuentra el sistema de archivos actual.

Por ejemplo, para recuperar archivos borrados en la
segunda partición del primer disco scsi en Linux,
usaríamos el siguiente nombre de ruta:

    /#undel:sda2

Esto le llevaría un tiempo a undelfs para cargar la
información antes de empezar a navegar por los archivos
allí contenidos.[EXTernal File System]
Sistema de archivos EXTerno (extfs)

extfs permite incorporar a GNU Midnight Commander
numerosas utilidades y tipos de archivos de manera
sencilla, simplemente escribiendo guiones (scripts).

Los sistemas de archivos Extfs son de dos tipos:

1. Sistemas de archivos autónomos, que no están asociados
a ningún archivo existente. Representan algún tipo de
información relacionada con el sistema en forma de árbol
de directorios. Se accede a ellos ejecutando 'cd
#nombrefs' donde nombrefs es el nombre corto que
identifica el extfs (ver más adelante). Ejemplos de éstos
son audio (lista de pistas de sonido en el CD) o apt
(lista de paquetes de tipo Debian en el sistema).

Por ejemplo, para listar las pistas de música del CD,
escribir

  cd #audio

2. Sistemas de archivos en un archivo (como rpm, patchfs y
más), que muestran los contenidos de un archivo en forma
de árbol de directorios. Puede tratarse de archivos reales
empaquetados o comprimidos en un archivo (urar, rpm) o
archivos virtuales, como puede ser el caso de mensajes en
un archivo de correo electrónico (mailfs) o partes de un
archivo de modificaciones o parches (patchfs). Para
acceder a ellos se añade '#nombrefs' al nombre del archivo
a abrir. Este archivo podría él mismo estar en otro
sistema de archivos virtual.

Por ejemplo, para listar los contenidos de un archivo
documentos.zip comprimido hay que escribir

  cd documentos.zip#uzip

En muchos aspectos, se puede tratar un sistema de archivos
externo como cualquier otro directorio. Podríamos añadirlo
a la lista de favoritos o cambiar a él desde la historia
de directorios. Una limitación importante es que, estando
dentro de él, no se puede ejecutar órdenes del sistema,
como por otra parte ocurre en cualquier sistema de
archivos VFS no local.

Midnigth Commander incluye inicialmente guiones para
algunos sistemas de archivos externos:

a       acceder a un disquete DOS/Windows 'A:' (cd #a).

apt     monitor del sistema de gestión de paquetes APT de
        Debian (cd #apt).

audio   acceso y audición de CDs (cd #audio o cd
        dispositivo#audio).

bpp     paquete de la distribución GNU/Linux Bad Penguin
        (cd archivo.bpp#bpp).

deb     paquete de la distribución GNU/Linux Debian (cd
        archivo.deb#deb).

dpkg    paquetes instalados en Debian GNU/Linux (cd
        #deb).

hp48    ver o copiar archivos a/desde una calculadora
        HP48 (cd #hp48).

lslR    navegación en listados lslR empleados en
        bastantes sitios FTP (cd filename#lslR).

mailfs  soporte para archivos de correo electrónico tipo
        mbox (cd archivo_mbox#mailfs).

patchfs manipulación de archivos de cambios/parches tipo
        diff (cd archivo#patchfs).

rpm     paquete RPM (cd archivo#rpm).

rpms    base de datos de paquetes RPM instalados (cd
        #rpms).

ulha, urar, uzip, uzoo, uar, uha
        herramientas de compresión (cd archivo#xxxx
        siendo xxxx uno de estos: ulha, urar, uzip, uzoo,
        uar, uha).

Se pueden asociar extensiones o tipos de archivo a un
determinado sistema de archivos externo tal como se
describe en la sección sobre cómo Editar el Archivo de
ExtensionesExtension File Edit de Midnight Commander. He aquí, a modo de
ejemplo, una entrada para paquetes Debian:

  regex/.deb$
          Open=%cd %p#deb
[Colors]
Colores

Midnight Commander intentará determinar si nuestro
terminal soporta el uso de color utilizando la base de
datos de terminales y nuestro nombre de terminal. Algunas
veces estará confundido, por lo que deberemos forzar el
modo en color o deshabilitar el modo de color usando el
argumento -c y -b respectivamente.

Si el programa está compilado con el gestor pantallas
Slang en lugar de ncurses, también chequeará la variable
COLORTERM, si existe, lo que tiene el mismo efecto que la
opción -c.

Podemos especificar a los terminales que siempre fuercen
el modo en color añadiendo la variable color_terminals a
la sección Colors del archivo de inicialización. Esto
evitará que Midnight Commander intente la detección de
soporte de color. Ejemplo:

[Colors]
color_terminals=linux,xterm
color_terminals=nombre-terminal1,nombre-terminal2...

El programa puede compilarse con ncurses y slang, ncurses
no ofrece la posibilidad de forzar el modo en color:
ncurses utiliza la información de la base de datos de
terminales.

Midnight Commander ofrece una forma de cambiar los colores
por defecto. Actualmente los colores se configuran a
través de la variable de entorno MC_COLOR_TABLE o en la
sección Colors del archivo de inicialización.

En la sección Colors, el mapa de colores por defecto se
carga desde la variable base_color. Podemos especificar un
mapa de colores alternativo para un terminal utilizando el
nombre del terminal como clave en esta sección. Ejemplo:

[Colors]
base_color=
xterm=menu=magenta:marked=,magenta:markselect=,red

El formato de la definición de color es:

  <PalabraClave>=<ColorTexto>,<ColorFondo>:<PalabraClave>= ...

los colores son opcionales, y las palabras claves son:
normal, selected, marked, markselect, errors, input,
reverse menu, menusel, menuhot, menuhotsel, gauge; los
colores por defecto son: dnormal, dfocus, dhotnormal,
dhotfocus; Los colores de Ayuda son: helpnormal,
helpitalic, helpbold, helplink, helpslink; Color del
visor: viewunderline; Modo especial resaltado: executable,
directory, link, stalelink, device, special, core. Colores
del editor: editnormal, editbold, editmarked.

Los cuadros de diálogo usan los siguientes colores:
dnormal usado para el texto normal, dfocus usado para el
componente actualmente seleccionado, dhotnormal usado para
diferenciar el color de la tecla activa en los componentes
normales, mientras que el color dhotfocus se utiliza para
el color resaltado en el componente seleccionado.

Los menús utilizan el mismo esquema equivalente con los
nombres menu, menusel, menuhot and menuhotsel en lugar de
los anteriores.

La ayuda utiliza los siguientes colores: helpnormal texto
normal, helpitalic utilizado para el texto enfatizado con
letra itálica en la página del manual, helpbold usado para
el texto enfatizado en negrita en la página del manual,
helplink usado para los hiperenlaces no seleccionados y
helpslink es utilizado para el hiperenlace seleccionado.

gauge (indicador) determina el color de la parte
completada de la barra de progresión (gauge), que muestra
qué porcentaje de archivos fueron copiados etc. de modo
gráfico.

Para el modo de resaltado del tipo de archivos, directory
especifica el color con que se muestran los directorios;
executable para los archivos ejecutables; link usado para
representar enlaces; device para dispositivos de
caracteres y de bloque; special para archivos especiales,
tales como colas (FIFO) e IPC sockets; core es para los
archivos volcados (véase también la opción highlight_mode
en la sección sobre Ajustes EspecialesSpecial Settings ).

Los colores posibles son: negro (black), gris (gray), rojo
(red), rojo brillante (brightred), verde (green), verde
claro (brightgreen), marrón (brown), amarillo (yellow),
azul oscuro (blue), azul brillante (brightblue), rosa
(magenta), rosa claro (brightmagenta), azul celeste
(cyan), celeste claro (brightcyan), gris claro (lightgray)
y blanco (white). Hay una palabra clave especial para
obtener un fondo transparente. Se trata de 'default'.
'default' solo se puede utilizar para en el color de
fondo. Ejemplo:

[Colors]
base_color=normal=white,default:marked=magenta,default
[Special Settings]
Ajustes Especiales

La mayoría de las opciones de Midnight Commander pueden
cambiarse desde los menús. Sin embargo, hay un pequeño
número de ajustes para los que es necesario editar el
archivo de configuración.

Estas variables se pueden cambiar en nuestro archivo
~/.mc/ini:

clear_before_exec

        Por defecto Midnight Commander limpia la pantalla
        antes de ejecutar un comando. Si preferimos ver
        la salida del comando en la parte inferior de la
        pantalla, editaremos nuestro archivo ~/mc.ini y
        cambiaremos el valor del campo clear_before_exec
        a 0.

confirm_view_dir

        Al pulsar F3 en un directorio, normalmente MC
        entra en ese directorio. Si este valor está a 1,
        entonces MC pedirá confirmación antes de cambiar
        el directorio si tenemos archivos marcados.

ftpfs_retry_seconds

        Este valor es el número de segundos que Midnight
        Commander esperará antes de intentar volver a
        conectar con un servidor de ftp que ha denegado
        el acceso. Si el valor es cero, el programa no
        reintentará el acceso.

ftpfs_use_passive_connections

        Esta opción está desactivada por defecto. Hace
        que el código de FTPfs utilice el modo de
        apertura pasivo para transferir archivos. Esto es
        usado por aquellos que están detrás de un
        encaminador con filtrado de paquetes. Esta opción
        sólo funciona si estamos utilizando un proxy para
        ftp.

max_dirt_limit

        Especifica cuántas actualizaciones de pantalla
        pueden saltarse al menos en el visor de archivos
        interno. Normalmente este valor no es
        significativo, porque el código automáticamente
        ajusta el número de actualizaciones a saltar de
        acuerdo al volumen de pulsaciones de teclas
        recibidas. Empero, en máquinas muy lentas o en
        terminales con autorepetición de teclado rápida,
        un valor grande puede hacer que la pantalla se
        actualice dando saltos.

        Parece ser que poniendo max_dirt_limit a 10
        produce el mejor comportamiento, y éste es el
        valor por defecto.

mouse_move_pages

        Controla cuándo el desplazamiento de pantalla
        realizado con el ratón se realiza por páginas o
        línea a línea en los paneles.

mouse_move_pages_viewer

        Controla cuándo el desplazamiento de pantalla
        realizado con el ratón se realiza por páginas o
        línea a línea en el visor de archivos interno.

old_esc_mode

        Por defecto Midnight Commander trata la tecla ESC
        como prefijo de tecla (old_esc_mode=0), si
        activamos esta opción (old_esc_mode=1), entonces
        la tecla ESC actuará como prefijo de tecla
        durante un segundo, y si no hay pulsaciones,
        entonces ESC será interpretado como la tecla de
        cancelación (ESC ESC).

only_leading_plus_minus

        Produce un tratamiento especial para '+', '-',
        '*' en la línea de órdenes (seleccionar,
        deseleccionar, selección inversa) sólo si la
        línea de órdenes está vacía. No necesitamos
        entrecomillar estos caracteres en la línea de
        órdenes. Pero no podremos cambiar la selección
        cuando la línea de órdenes no esté vacía.

panel_scroll_pages

        Si existe (por defecto), el panel se desplazará
        media pantalla cuando el cursor alcance el final
        o el principio del panel, en otro caso se
        desplazará un archivo cada vez.

show_output_starts_shell

        Esta variable sólo funciona si no se utiliza el
        soporte de subshell. Cuando utilizamos la
        combinación C-o para volver a la pantalla de
        usuario, si está activada, tendremos un nuevo
        shell. De otro modo, pulsando cualquier tecla nos
        devolverá a Midnight Commander.

torben_fj_mode

        Si este modificador existe, entonces las teclas
        Inicio y Fin funcionarán de manera diferente en
        los paneles, en lugar de mover la selección al
        primer o último archivo en los paneles, actuarán
        como sigue:

        La tecla Inicio: Irá a la línea central del
        panel, si está bajo ella; sino va a la primera
        línea a menos que ya esté allí, en este caso irá
        al primer archivo del panel.

        La tecla Fin tiene un comportamiento similar: Irá
        a la línea central del panel, si está situada en
        la mitad superior del panel; si no irá a la línea
        inferior del panel a menos que ya estemos ahí, en
        cuyo caso moverá la selección al último nombre de
        archivo del panel.

use_file_to_guess_type

        Si esta variable está activada (por defecto lo
        está) se recurrirá al comando "file" para
        reconocer los tipos de archivo referidos en el
        archivo mc.extExtension File Edit.

xterm_mode

        Si esta variable está activada (por defecto no)
        cuando naveguemos por el sistema de archivos en
        un panel en árbol, se irá actualizando
        automáticamente el otro panel con los contenidos
        del directorio seleccionado en cada momento.[Terminal databases]
Ajustes del Terminal

Midnight Commander permite hacer ajustes a la base de
datos de terminales del sistema sin necesidad de
privilegios de superusuario. El programa busca
definiciones de teclas en el archivo de inicialización del
sistema /usr/share/mc/mc.lib o en el del usuario
~/.mc/ini, en la sección "terminal:nuestro-terminal" y si
no en "terminal:general". Cada línea comienza con el
identificador de la tecla, seguido de un signo de igual y
la definición de la tecla. Para representar el carácter de
escape se utiliza \e y ^x para el carácter control-x.

Los identificadores de tecla son:

f0 a f20      teclas de función f0 a f20
bs            tecla de borrado
home          tecla de inicio
end           tecla de fin
up            tecla de cursor arriba
down          tecla de cursor abajo
left          tecla de cursor izquierda
right         tecla de cursor derecha
pgdn          tecla de avance de página
pgup          tecla de retroceso de página
insert        tecla de insertar
delete        tecla de suprimir
complete      tecla para completar

Ejemplo: para indicar que la secuencia Escape + [ + O + p
corresponde a la tecla de insertar, hay que colocar en el
archivo ~/.mc/ini:

insert=\e[Op

El identificador complete representa la secuencia usada
para invocar el mecanismo de completar nombres. Esto se
hace habitualmente con M-tabulador, pero podemos
configurar otras teclas para esta función, especialmente
en teclados que incorporan tantas teclas especiales
(bonitas pero inútiles o infrautilizadas).

[FILES]
ARCHIVOS AUXILIARES

Los directorios indicados a continuación pueden variar de
una instalación a otra. También se pueden modificar con la
variable de entorno MC_DATADIR, que de estar definida se
emplearía en vez de /usr/share/mc.

/usr/share/mc.hlp

        Archivo de ayuda.

/usr/share/mc/mc.ext

        Archivo de extensiones por defecto del sistema.

~/.mc/bindings

        Archivo de usuario de extensiones y configuración
        de visor y editor. Si está presente prevalece
        sobre el contenido de los archivos del sistema.

/usr/share/mc/mc.ini

        Archivo de configuración del sistema para
        Midnight Commander, sólo si el usuario no dispone
        de su propio ~/.mc/ini.

/usr/share/mc/mc.lib

        Opciones globales de Midnight Commander. Se
        aplican siempre a todos los usuarios, tengan
        ~/.mc/ini o no. Actualmente sólo se emplea para
        los ajustes de terminalTerminal databases.

~/.mc/ini

        Configuración personal del usuario. Si este
        archivo está presente entonces se cargará la
        configuración desde aquí en lugar de desde el
        archivo de configuración del sistema.

/usr/share/mc/mc.hint

        Este archivo contiene los mensajes cortos de
        ayuda mostrados por el programa.

/usr/share/mc/mc.menu

        Este archivo contiene el menú de aplicaciones por
        defecto para el sistema.

~/.mc/menu

        Menú de aplicaciones personal del usuario. Si
        está presente será utilizado en lugar del menú
        por defecto del sistema.

~/.mc/Tree

        La lista de directorios para el árbol de
        directorios y la vista en árbol.

./.mc.menu

        Menú local definido por el usuario. Si este
        archivo está presente será usado en lugar del
        menú de aplicaciones personal o de sistema.[AVAILABILITY]
DISPONIBILIDAD

La última versión de este programa puede encontrarse en
ftp://ftp.ibiblio.org/pub/Linux/utils/file/managers/mc/.[SEE ALSO]
VÉASE TAMBIÉN

mcedit(1), mcserv(8), sh(1), bash(1), tcsh(1), zsh(1),
ed(1), view(1), terminfo(1), gpm(1).

La página web de Midnight Commander está en:
	http://www.ibiblio.org/mc/

La presente documentación recoge información relativa a la
versión 4.6.1 (Enero de 2004). Esta traducción no está
completamente actualizada con la versión original en
inglés. Para acceder a información sobre versiones
recientes consultar la página de manual en inglés que
contiene información más completa y actualizada. Para ver
el susodicho manual original ejecutar en la línea de
órdenes:
        LANG= LC_ALL= man mc
[AUTHORS]
AUTORES

Los autores y contribuciones se recogen en el archivo
AUTHORS de la distribución.[BUGS]
ERRORES

Véase el archivo "TODO" en la distribución para saber qué
falta por hacer.

Para informar de problemas con el programa, envíar un
mensaje a la dirección: mc-devel@gnome.org.

Se debe proporcionar una descripción detallada del
problema, la versión del programa (se obtiene con 'mc -V')
y el sistema operativo utilizados. Si el programa
revienta, sería también útil disponer del estado de la
pila.[TRANSLATION]
TRADUCCIÓN

Francisco Gabriel Aroca, 1998. Reformateado y actualizado
por David Martín, 2002-2004.

Midnight Commander traducido a castellano por David Martín
<dmartina@excite.com>.

[main]
 lqwqk     k           k     
 x x x .   x     .     x     
 x x x k lqu wqk k lqw tqk n 
 x x x x x x x x x x x x x x 
 v   v v mqv v v v mqu v v mj
     qqqqqqCommanderqj 

Ésta es la pantalla de inicio de la ayuda de
GNU Midnight Commander.

Puede pulsar la tecla IntroHow to use help para aprender a navegar por el
sistema de ayuda, o acceder directamente a los contenidosContents.

GNU Midnight Commander es obra de sus numerosos autoresAUTHORS.

GNU Midnight Commander NO INCLUYE NINGÚN TIPO DE GARANTÍAWarranty,
es software libre, y se alienta su redistribución en los
terminos y condiciones que están contenidos en la Licencia
Pública General de GNU (GPL)Licencia GNU, de la que existe una
traducción no oficial al españolLicencia GNU (Español).[Licencia GNU]

                GNU GENERAL PUBLIC LICENSE
                   Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

 Everyone is permitted to copy and distribute verbatim
copies of this license document, but changing it is not
allowed.

                         Preamble

  The licenses for most software are designed to take away
your freedom to share and change it.  By contrast, the GNU
General Public License is intended to guarantee your
freedom to share and change free software--to make sure
the software is free for all its users.  This General
Public License applies to most of the Free Software
Foundation's software and to any other program whose
authors commit to using it.  (Some other Free Software
Foundation software is covered by the GNU Library General
Public License instead.)  You can apply it to your
programs, too.

  When we speak of free software, we are referring to
freedom, not price.  Our General Public Licenses are
designed to make sure that you have the freedom to
distribute copies of free software (and charge for this
service if you wish), that you receive source code or can
get it if you want it, that you can change the software or
use pieces of it in new free programs; and that you know
you can do these things.

  To protect your rights, we need to make restrictions
that forbid anyone to deny you these rights or to ask you
to surrender the rights.  These restrictions translate to
certain responsibilities for you if you distribute copies
of the software, or if you modify it.

  For example, if you distribute copies of such a program,
whether gratis or for a fee, you must give the recipients
all the rights that you have.  You must make sure that
they, too, receive or can get the source code.  And you
must show them these terms so they know their rights.

  We protect your rights with two steps: (1) copyright the
software, and (2) offer you this license which gives you
legal permission to copy, distribute and/or modify the
software.

  Also, for each author's protection and ours, we want to
make certain that everyone understands that there is no
warranty for this free software.  If the software is
modified by someone else and passed on, we want its
recipients to know that what they have is not the
original, so that any problems introduced by others will
not reflect on the original authors' reputations.

  Finally, any free program is threatened constantly by
software patents.  We wish to avoid the danger that
redistributors of a free program will individually obtain
patent licenses, in effect making the program proprietary.
To prevent this, we have made it clear that any patent
must be licensed for everyone's free use or not licensed
at all.

  The precise terms and conditions for copying,
distribution and modification follow.

                GNU GENERAL PUBLIC LICENSE
            TERMS AND CONDITIONS FOR COPYING,
              DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work
which contains a notice placed by the copyright holder
saying it may be distributed under the terms of this
General Public License.  The "Program", below, refers to
any such program or work, and a "work based on the
Program" means either the Program or any derivative work
under copyright law: that is to say, a work containing the
Program or a portion of it, either verbatim or with
modifications and/or translated into another language.
(Hereinafter, translation is included without limitation
in the term "modification".)  Each licensee is addressed
as "you".

Activities other than copying, distribution and
modification are not covered by this License; they are
outside its scope.  The act of running the Program is not
restricted, and the output from the Program is covered
only if its contents constitute a work based on the
Program (independent of having been made by running the
Program).  Whether that is true depends on what the
Program does.

  1. You may copy and distribute verbatim copies of the
Program's source code as you receive it, in any medium,
provided that you conspicuously and appropriately publish
on each copy an appropriate copyright notice and
disclaimer of warranty; keep intact all the notices that
refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of
this License along with the Program.

You may charge a fee for the physical act of transferring
a copy, and you may at your option offer warranty
protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or
any portion of it, thus forming a work based on the
Program, and copy and distribute such modifications or
work under the terms of Section 1 above, provided that you
also meet all of these conditions:

    a) You must cause the modified files to carry
prominent notices stating that you changed the files and
the date of any change.

    b) You must cause any work that you distribute or
publish, that in whole or in part contains or is derived
from the Program or any part thereof, to be licensed as a
whole at no charge to all third parties under the terms of
this License.

    c) If the modified program normally reads commands
interactively when run, you must cause it, when started
running for such interactive use in the most ordinary way,
to print or display an announcement including an
appropriate copyright notice and a notice that there is no
warranty (or else, saying that you provide a warranty) and
that users may redistribute the program under these
conditions, and telling the user how to view a copy of
this License.  (Exception: if the Program itself is
interactive but does not normally print such an
announcement, your work based on the Program is not
required to print an announcement.)

These requirements apply to the modified work as a whole.
If identifiable sections of that work are not derived from
the Program, and can be reasonably considered independent
and separate works in themselves, then this License, and
its terms, do not apply to those sections when you
distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a
work based on the Program, the distribution of the whole
must be on the terms of this License, whose permissions
for other licensees extend to the entire whole, and thus
to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights
or contest your rights to work written entirely by you;
rather, the intent is to exercise the right to control the
distribution of derivative or collective works based on
the Program.

In addition, mere aggregation of another work not based on
the Program with the Program (or with a work based on the
Program) on a volume of a storage or distribution medium
does not bring the other work under the scope of this
License.

  3. You may copy and distribute the Program (or a work
based on it, under Section 2) in object code or executable
form under the terms of Sections 1 and 2 above provided
that you also do one of the following:

    a) Accompany it with the complete corresponding
machine-readable source code, which must be distributed
under the terms of Sections 1 and 2 above on a medium
customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at
least three years, to give any third party, for a charge
no more than your cost of physically performing source
distribution, a complete machine-readable copy of the
corresponding source code, to be distributed under the
terms of Sections 1 and 2 above on a medium customarily
used for software interchange; or,

    c) Accompany it with the information you received as
to the offer to distribute corresponding source code.
(This alternative is allowed only for noncommercial
distribution and only if you received the program in
object code or executable form with such an offer, in
accord with Subsection b above.)

The source code for a work means the preferred form of the
work for making modifications to it.  For an executable
work, complete source code means all the source code for
all modules it contains, plus any associated interface
definition files, plus the scripts used to control
compilation and installation of the executable.  However,
as a special exception, the source code distributed need
not include anything that is normally distributed (in
either source or binary form) with the major components
(compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself
accompanies the executable.

If distribution of executable or object code is made by
offering access to copy from a designated place, then
offering equivalent access to copy the source code from
the same place counts as distribution of the source code,
even though third parties are not compelled to copy the
source along with the object code.

  4. You may not copy, modify, sublicense, or distribute
the Program except as expressly provided under this
License.  Any attempt otherwise to copy, modify,
sublicense or distribute the Program is void, and will
automatically terminate your rights under this License.
However, parties who have received copies, or rights, from
you under this License will not have their licenses
terminated so long as such parties remain in full
compliance.

  5. You are not required to accept this License, since
you have not signed it.  However, nothing else grants you
permission to modify or distribute the Program or its
derivative works.  These actions are prohibited by law if
you do not accept this License.  Therefore, by modifying
or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to
do so, and all its terms and conditions for copying,
distributing or modifying the Program or works based on
it.

  6. Each time you redistribute the Program (or any work
based on the Program), the recipient automatically
receives a license from the original licensor to copy,
distribute or modify the Program subject to these terms
and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights
granted herein.  You are not responsible for enforcing
compliance by third parties to this License.

  7. If, as a consequence of a court judgment or
allegation of patent infringement or for any other reason
(not limited to patent issues), conditions are imposed on
you (whether by court order, agreement or otherwise) that
contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you
cannot distribute so as to satisfy simultaneously your
obligations under this License and any other pertinent
obligations, then as a consequence you may not distribute
the Program at all.  For example, if a patent license
would not permit royalty-free redistribution of the
Program by all those who receive copies directly or
indirectly through you, then the only way you could
satisfy both it and this License would be to refrain
entirely from distribution of the Program.

If any portion of this section is held invalid or
unenforceable under any particular circumstance, the
balance of the section is intended to apply and the
section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to
infringe any patents or other property right claims or to
contest validity of any such claims; this section has the
sole purpose of protecting the integrity of the free
software distribution system, which is implemented by
public license practices.  Many people have made generous
contributions to the wide range of software distributed
through that system in reliance on consistent application
of that system; it is up to the author/donor to decide if
he or she is willing to distribute software through any
other system and a licensee cannot impose that choice.

This section is intended to make thoroughly clear what is
believed to be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is
restricted in certain countries either by patents or by
copyrighted interfaces, the original copyright holder who
places the Program under this License may add an explicit
geographical distribution limitation excluding those
countries, so that distribution is permitted only in or
among countries not thus excluded.  In such case, this
License incorporates the limitation as if written in the
body of this License.

  9. The Free Software Foundation may publish revised
and/or new versions of the General Public License from
time to time.  Such new versions will be similar in spirit
to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If
the Program specifies a version number of this License
which applies to it and "any later version", you have the
option of following the terms and conditions either of
that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a
version number of this License, you may choose any version
ever published by the Free Software Foundation.

  10. If you wish to incorporate parts of the Program into
other free programs whose distribution conditions are
different, write to the author to ask for permission.  For
software which is copyrighted by the Free Software
Foundation, write to the Free Software Foundation; we
sometimes make exceptions for this.  Our decision will be
guided by the two goals of preserving the free status of
all derivatives of our free software and of promoting the
sharing and reuse of software generally.

[Warranty]
                       NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE,
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT
PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED
IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE
QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR
AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY
OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM
AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY
TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED
BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR
OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.

               END OF TERMS AND CONDITIONS

      How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of
the greatest possible use to the public, the best way to
achieve this is to make it free software which everyone
can redistribute and change under these terms.

  To do so, attach the following notices to the program.
It is safest to attach them to the start of each source
file to most effectively convey the exclusion of warranty;
and each file should have at least the "copyright" line
and a pointer to where the full notice is found.

<one line to give the program's name and a brief idea of
what it does.>
Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it
and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any
later version.

    This program is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

    You should have received a copy of the GNU General
Public License along with this program; if not, write to
the Free Software Foundation, Inc., 51 Franklin Street,
Fifth Floor, Boston, MA  02110-1301  USA

Also add information on how to contact you by electronic
and paper mail.

If the program is interactive, make it output a short
notice like this when it starts in an interactive mode:

Gnomovision version 69, Copyright (C) year name of author
Gnomovision comes with ABSOLUTELY NO WARRANTY; for details
type `show w'.  This is free software, and you are welcome
to redistribute it under certain conditions; type `show c'
for details.

The hypothetical commands `show w' and `show c' should
show the appropriate parts of the General Public License.
Of course, the commands you use may be called something
other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a
programmer) or your school, if any, to sign a "copyright
disclaimer" for the program, if necessary.  Here is a
sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest
in the program `Gnomovision' (which makes passes at
compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating
your program into proprietary programs.  If your program
is a subroutine library, you may consider it more useful
to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU
Library General Public License instead of this License.

[Licencia GNU (Español)]

Licencia Pública GNU

Esta  es  la conocida como GNU Public License (GPL), versión 2
(de junio de 1.991), que cubre la mayor parte del software  de
la Free Software Foundation, y muchos más programas.

---

NOTA IMPORTANTE:

Esta es una traducción no oficial al español de la GNU General
Public LicenseLicencia GNU.

No ha sido publicada por la Free  Software  Foundation,  y  no
establece  legalmente  las condiciones de distribución para el
software que usa la GNU GPL. Estas condiciones  se  establecen
solamente por el texto original, en inglés, de la GNU GPL. Sin
embargo,  esperamos  que   esta   traducción   ayude   a   los
hispanohablantes a entender mejor la GNU GPL.


IMPORTANT NOTICE:

This  is  an  unofficial translation of the GNU General Public
License into  Spanish.  It  was  not  published  by  the  Free
Software   Foundation,   and   does   not  legally  state  the
distribution terms for software that uses  the  GNU  GPL--only
the  original  English text of the GNU GPL does that. However,
we hope that  this  translation  will  help  Spanish  speakers
understand the GNU GPL better.

---

Copyright  (C)  1989,  1991 Free Software Foundation, Inc.  51
Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Se permite la copia y distribución de copias literales de este
documento, pero no se permite su modificación.

Preámbulo

Las  licencias  que  cubren  la mayor parte del software están
diseñadas para quitarle a usted la libertad de  compartirlo  y
modificarlo.  Por el contrario, la Licencia Pública General de
GNU pretende garantizarle la libertad de compartir y modificar
software  libre,  para  asegurar que el software es libre para
todos sus usuarios. Esta Licencia Pública General se aplica  a
la mayor parte del software de la Free Software Foundation y a
cualquier otro  programa  si  sus  autores  se  comprometen  a
utilizarla.   (Existe   otro  software  de  la  Free  Software
Foundation que está cubierto por la Licencia  Pública  General
de GNU para Bibliotecas). Si quiere, también puede aplicarla a
sus propios programas.

Cuando hablamos de software  libre,  estamos  refiriéndonos  a
libertad,  no  a precio. Nuestras Licencias Públicas Generales
están diseñadas para asegurarnos de que tenga la  libertad  de
distribuir copias de software libre (y cobrar por ese servicio
si quiere), de  que  reciba  el  código  fuente  o  que  pueda
conseguirlo si lo quiere, de que pueda modificar el software o
usar fragmentos de él en nuevos programas  libres,  y  de  que
sepa que puede hacer todas estas cosas.

Para  proteger  sus derechos necesitamos algunas restricciones
que prohiban a cualquiera negarle a  usted  estos  derechos  o
pedirle  que renuncie a ellos. Estas restricciones se traducen
en ciertas obligaciones que le afectan  si  distribuye  copias
del software, o si lo modifica.

Por  ejemplo,  si distribuye copias de uno de estos programas,
sea gratuitamente, o a cambio de  una  contraprestación,  debe
dar  a  los  receptores  todos  los  derechos  que tiene. Debe
asegurarse de que ellos también reciben, o  pueden  conseguir,
el código fuente. Y debe mostrarles estas condiciones de forma
que conozcan sus derechos.

Protegemos sus derechos con la combinación de dos medidas:

1. Ponemos el software bajo copyright y

2. le ofrecemos esta licencia, que le da  permiso  legal  para
copiar, distribuir y/o modificar el software.

También, para la protección de cada autor y la nuestra propia,
queremos asegurarnos de que todo el mundo comprende que no  se
proporciona  ninguna  garantía para este software libre. Si el
software se modifica  por  cualquiera  y  éste  a  su  vez  lo
distribuye,  queremos  que  sus  receptores  sepan  que lo que
tienen no es el original,  de  forma  que  cualquier  problema
introducido por otros no afecte a la reputación de los autores
originales.

Por  último,  cualquier  programa  libre  está  constantemente
amenazado  por  patentes sobre el software. Queremos evitar el
peligro de que  los  redistribuidores  de  un  programa  libre
obtengan  patentes  por  su  cuenta,  convirtiendo de facto el
programa en propietario. Para evitar esto, hemos dejado  claro
que  cualquier  patente  debe  ser pedida para el uso libre de
cualquiera, o no ser pedida.

Los  términos  exactos  y  las  condiciones  para  la   copia,
distribución y modificación se exponen a continuación.

Términos   y   condiciones   para  la  copia,  distribución  y
modificación

1. Esta Licencia se aplica a cualquier programa u otro tipo de
trabajo  que  contenga  una  nota  colocada por el tenedor del
copyright diciendo que puede ser distribuido bajo los términos
de  esta  Licencia Pública General. En adelante, «Programa» se
referirá  a  cualquier  programa  o  trabajo  que  cumpla  esa
condición  y  «trabajo basado en el Programa» se referirá bien
al Programa o a cualquier trabajo derivado de él según la  ley
de  copyright.  Esto es, un trabajo que contenga el programa o
una porción de él, bien en forma literal o con  modificaciones
y/o  traducido  en otro lenguaje.  Por lo tanto, la traducción
está incluida sin limitaciones en el  término  «modificación».
Cada concesionario (licenciatario) será denominado «usted».

Cualquier  otra  actividad que no sea la copia, distribución o
modificación no está cubierta por esta Licencia, está fuera de
su   ámbito.   El   acto  de  ejecutar  el  Programa  no  está
restringido, y los resultados  del  Programa  están  cubiertos
únicamente  si sus contenidos constituyen un trabajo basado en
el Programa, independientemente de haberlo producido  mediante
la  ejecución  del programa. El que esto se cumpla, depende de
lo que haga el programa.

2. Usted puede copiar y distribuir copias literales del código
fuente  del  Programa,  según  lo  has  recibido, en cualquier
medio, supuesto que de forma adecuada y bien visible  publique
en cada copia un anuncio de copyright adecuado y un repudio de
garantía, mantenga intactos todos los anuncios que se refieran
a  esta  Licencia y a la ausencia de garantía, y proporcione a
cualquier  otro  receptor  del  programa  una  copia  de  esta
Licencia junto con el Programa.

Puede  cobrar  un  precio por el acto físico de transferir una
copia, y puede, según su libre albedrío,  ofrecer  garantía  a
cambio de unos honorarios.

3.  Puede  modificar  su  copia  o  copias  del  Programa o de
cualquier porción de él, formando de esta  manera  un  trabajo
basado  en el Programa, y copiar y distribuir esa modificación
o  trabajo  bajo  los  términos  del  apartado  1,  antedicho,
supuesto que además cumpla las siguientes condiciones:

a.  Debe  hacer  que  los ficheros modificados lleven anuncios
prominentes indicando que  los  ha  cambiado  y  la  fecha  de
cualquier cambio.

b.  Debe hacer que cualquier trabajo que distribuya o publique
y que en todo o en parte contenga o sea derivado del  Programa
o  de  cualquier  parte de él sea licenciada como un todo, sin
carga alguna, a todas las terceras partes y bajo los  términos
de esta Licencia.

c.   Si   el   programa  modificado  lee  normalmente  órdenes
interactivamente cuando es ejecutado, debe hacer  que,  cuando
comience su ejecución para ese uso interactivo de la forma más
habitual, muestre o escriba un mensaje que incluya un  anuncio
de copyright y un anuncio de que no se ofrece ninguna garantía
(o por el contrario que sí  se  ofrece  garantía)  y  que  los
usuarios   pueden   redistribuir   el   programa   bajo  estas
condiciones, e indicando al usuario cómo ver una copia de esta
licencia.  (Excepción:  si  el  propio programa es interactivo
pero normalmente no muestra ese anuncio, no se requiere que su
trabajo basado en el Programa muestre ningún anuncio).

Estos  requisitos  se  aplican  al  trabajo modificado como un
todo. Si partes identificables de ese trabajo no son derivadas
del  Programa,  y  pueden,  razonablemente,  ser  consideradas
trabajos independientes y separados por ellos mismos, entonces
esta  Licencia  y  sus  términos  no  se aplican a esas partes
cuando sean distribuidas como trabajos separados. Pero  cuando
distribuya esas mismas secciones como partes de un todo que es
un trabajo basado en el Programa,  la  distribución  del  todo
debe  ser  según los términos de esta licencia, cuyos permisos
para otros licenciatarios se extienden al todo completo, y por
lo  tanto  a todas y cada una de sus partes, con independencia
de quién la escribió.

Por lo tanto, no es la intención  de  este  apartado  reclamar
derechos  o  desafiar  sus  derechos  sobre  trabajos escritos
totalmente por usted mismo. El intento es ejercer el derecho a
controlar  la  distribución de trabajos derivados o colectivos
basados en el Programa.

Además, el simple hecho de reunir un trabajo no basado  en  el
Programa  con  el  Programa  (o  con  un  trabajo basado en el
Programa) en un volumen de almacenamiento o  en  un  medio  de
distribución no hace que dicho trabajo entre dentro del ámbito
cubierto por esta Licencia.

4. Puede copiar y distribuir el Programa (o un trabajo  basado
en  él,  según  se  especifica  en  el apartado 2, como código
objeto o en formato  ejecutable  según  los  términos  de  los
apartados  1  y  2,  supuesto  que  además  cumpla  una de las
siguientes condiciones:

a. Acompañarlo con el código fuente completo  correspondiente,
en  formato  electrónico,  que  debe  ser distribuido según se
especifica en los apartados 1 y 2 de esta Licencia en un medio
habitualmente utilizado para el intercambio de programas, o

b.  Acompañarlo  con una oferta por escrito, válida durante al
menos tres años, de proporcionar a cualquier tercera parte una
copia  completa  en  formato  electrónico  del  código  fuente
correspondiente, a un  coste  no  mayor  que  el  de  realizar
físicamente  la  distribución del fuente, que será distribuido
bajo  las  condiciones  descritas  en  los  apartados  1  y  2
anteriores,  en  un  medio  habitualmente  utilizado  para  el
intercambio de programas, o

c. Acompañarlo con la  información  que  recibiste  ofreciendo
distribuir  el  código fuente correspondiente. (Esta opción se
permite sólo para distribución no comercial y  sólo  si  usted
recibió el programa como código objeto o en formato ejecutable
con tal oferta, de acuerdo con el apartado b anterior).

Por código fuente de un trabajo se entiende la forma preferida
del trabajo cuando se le hacen modificaciones. Para un trabajo
ejecutable, se entiende por código  fuente  completo  todo  el
código  fuente  para  todos  los  módulos  que  contiene,  más
cualquier fichero asociado de definición  de  interfaces,  más
los   guiones  utilizados  para  controlar  la  compilación  e
instalación del ejecutable. Como excepción especial el  código
fuente   distribuido   no   necesita   incluir  nada  que  sea
distribuido normalmente  (bien  como  fuente,  bien  en  forma
binaria) con los componentes principales (compilador, kernel y
similares) del  sistema  operativo  en  el  cual  funciona  el
ejecutable,  a  no  ser  que  el propio componente acompañe al
ejecutable.

Si la distribución del ejecutable o del código objeto se  hace
mediante  la  oferta  acceso para copiarlo de un cierto lugar,
entonces se considera la  oferta  de  acceso  para  copiar  el
código  fuente  del  mismo  lugar como distribución del código
fuente, incluso aunque terceras partes  no  estén  forzadas  a
copiar el fuente junto con el código objeto.

5.  No  puede  copiar, modificar, sublicenciar o distribuir el
Programa  excepto  como  prevé  expresamente  esta   Licencia.
Cualquier   intento   de   copiar,  modificar  sublicenciar  o
distribuir el Programa de otra forma es inválida, y  hará  que
cesen  automáticamente  los  derechos  que te proporciona esta
Licencia. En cualquier caso, las  partes  que  hayan  recibido
copias  o  derechos  de usted bajo esta Licencia no cesarán en
sus derechos mientras esas partes continúen cumpliéndola.

6. No está obligado a aceptar esta licencia, ya que no  la  ha
firmado.   Sin  embargo,  no  hay  hada más que le proporcione
permiso para modificar o distribuir el Programa o sus trabajos
derivados.  Estas  acciones  están prohibidas por la ley si no
acepta esta Licencia.  Por lo tanto, si modifica o  distribuye
el  Programa (o cualquier trabajo basado en el Programa), está
indicando que acepta esta Licencia para poder hacerlo, y todos
sus términos y condiciones para copiar, distribuir o modificar
el Programa o trabajos basados en él.

7. Cada vez que redistribuya el Programa (o cualquier  trabajo
basado en el Programa), el receptor recibe automáticamente una
licencia del licenciatario original para copiar, distribuir  o
modificar  el  Programa,  de  forma  sujeta a estos términos y
condiciones. No puede imponer al receptor ninguna  restricción
más  sobre  el ejercicio de los derechos aquí garantizados. No
es usted  responsable  de  hacer  cumplir  esta  licencia  por
terceras partes.

8.  Si  como  consecuencia de una resolución judicial o de una
alegación de infracción de patente o por cualquier otra  razón
(no  limitada  a  asuntos  relacionados  con  patentes)  se le
imponen condiciones (ya sea por mandato judicial, por  acuerdo
o por cualquier otra causa) que contradigan las condiciones de
esta Licencia, ello no le exime de cumplir las condiciones  de
esta  Licencia.  Si  no puede realizar distribuciones de forma
que se satisfagan simultáneamente sus obligaciones  bajo  esta
licencia y cualquier otra obligación pertinente entonces, como
consecuencia, no  puede  distribuir  el  Programa  de  ninguna
forma.   Por   ejemplo,   si   una   patente   no  permite  la
redistribución libre de derechos de  autor  del  Programa  por
parte   de   todos  aquellos  que  reciban  copias  directa  o
indirectamente a través de usted, entonces la única  forma  en
que  podría  satisfacer tanto esa condición como esta Licencia
sería evitar completamente la distribución del Programa.

Si cualquier porción de este apartado se considera inválida  o
imposible  de  cumplir bajo cualquier circunstancia particular
ha de cumplirse el  resto  y  la  sección  por  entero  ha  de
cumplirse en cualquier otra circunstancia.

No  es  el  propósito  de  este apartado inducirle a infringir
ninguna reivindicación de patente ni de ningún otro derecho de
propiedad   o   impugnar  la  validez  de  ninguna  de  dichas
reivindicaciones. Este apartado tiene el  único  propósito  de
proteger la integridad del sistema de distribución de software
libre, que se realiza mediante prácticas de licencia  pública.
Mucha  gente  ha  hecho  contribuciones  generosas  a  la gran
variedad de software distribuido mediante ese sistema  con  la
confianza de que el sistema se aplicará consistentemente. Será
el autor/donante quien decida si  quiere  distribuir  software
mediante  cualquier  otro  sistema  y  una  licencia  no puede
imponer esa elección.

Este apartado pretende dejar completamente  claro  lo  que  se
cree que es una consecuencia del resto de esta Licencia.

9.  Si la distribución y/o uso de el Programa está restringida
en ciertos países, bien por patentes  o  por  interfaces  bajo
copyright,  el  tenedor del copyright que coloca este Programa
bajo esta Licencia puede añadir una  limitación  explícita  de
distribución  geográfica  excluyendo esos países, de forma que
la distribución se permita sólo  en  o  entre  los  países  no
excluidos   de   esta  manera.  En  ese  caso,  esta  Licencia
incorporará la limitación como  si  estuviese  escrita  en  el
cuerpo de esta Licencia.

10.  La  Free  Software  Foundation  puede  publicar versiones
revisadas y/o nuevas de la Licencia Pública General de  tiempo
en tiempo. Dichas nuevas versiones serán similares en espíritu
a la presente versión, pero pueden ser diferentes en  detalles
para considerar nuevos problemas o situaciones.

Cada  versión  recibe un número de versión que la distingue de
otras. Si el Programa especifica un número de versión de  esta
Licencia  que  se  refiere  a  ella  y  a  «cualquier  versión
posterior»,  tienes  la  opción  de  seguir  los  términos   y
condiciones,  bien  de  esa versión, bien de cualquier versión
posterior publicada por la Free  Software  Foundation.  Si  el
Programa  no especifica un número de versión de esta Licencia,
puedes  escoger  cualquier  versión  publicada  por  la   Free
Software Foundation.

11.   Si  quiere  incorporar  partes  del  Programa  en  otros
programas  libres  cuyas  condiciones  de   distribución   son
diferentes,  escribe  al  autor  para  pedirle  permiso. Si el
software tiene  copyright  de  la  Free  Software  Foundation,
escribe  a  la Free Software Foundation: algunas veces hacemos
excepciones en estos casos. Nuestra decisión estará guiada por
el  doble  objetivo  de  de preservar la libertad de todos los
derivados de nuestro software  libre  y  promover  el  que  se
comparta y reutilice el software en general.

AUSENCIA DE GARANTÍA

12. Como el programa se licencia libre de cargas, no se ofrece
ninguna garantía sobre el  programa,  en  todas  la  extensión
permitida  por  la  legislación  aplicable.  Excepto cuando se
indique de otra forma por escrito, los tenedores del copyright
y/u  otras  partes  proporcionan  el  programa «tal cual», sin
garantía de ninguna  clase,  bien  expresa  o  implícita,  con
inclusión,  pero  sin  limitación  a las garantías mercantiles
implícitas o a la conveniencia para un  propósito  particular.
Cualquier  riesgo  referente  a  la calidad y prestaciones del
programa es asumido por usted. Si se probase que  el  Programa
es   defectuoso,   asume   el  coste  de  cualquier  servicio,
reparación o corrección.

13. En ningún caso,  salvo  que  lo  requiera  la  legislación
aplicable o haya sido acordado por escrito, ningún tenedor del
copyright ni ninguna otra parte que modifique y/o redistribuya
el Programa según se permite en esta Licencia será responsable
ante usted  por  daños,  incluyendo  cualquier  daño  general,
especial,  incidental  o  resultante producido por el uso o la
imposibilidad de uso del Programa  (con  inclusión,  pero  sin
limitación  a la pérdida de datos o a la generación incorrecta
de datos o a pérdidas sufridas por usted o por terceras partes
o  a  un  fallo  del  Programa al funcionar en combinación con
cualquier otro programa), incluso  si  dicho  tenedor  u  otra
parte ha sido advertido de la posibilidad de dichos daños.

FIN DE TÉRMINOS Y CONDICIONES

Apéndice:  Cómo aplicar estos términos a sus nuevos programas.

Si usted desarrolla un nuevo Programa, y quiere  que  sea  del
mayor  uso  posible para el público en general, la mejor forma
de  conseguirlo  es  convirtiéndolo  en  software  libre   que
cualquiera pueda redistribuir y cambiar bajo estos términos.

Para  hacerlo,  añada  los siguientes anuncios al programa. Lo
más seguro es añadirlos al principio de  cada  fichero  fuente
para  transmitir  lo  más efectivamente posible la ausencia de
garantía. Además cada fichero debería tener al menos la  línea
de  «copyright»  y  un  indicador a dónde puede encontrarse el
anuncio completo.

<una línea para indicar el nombre del programa  y  una  rápida
idea de qué hace.>

Copyright (C) <año>  <nombre del autor>

Este  programa  es  software  libre.  Puede redistribuirlo y/o
modificarlo bajo los términos de la Licencia  Pública  General
de  GNU  según  es  publicada por la Free Software Foundation,
bien de la versión 2  de  dicha  Licencia  o  bien  (según  su
elección) de cualquier versión posterior.

Este  programa se distribuye con la esperanza de que sea útil,
pero SIN NINGUNA GARANTÍA, incluso sin la  garantía  MERCANTIL
implícita  o  sin garantizar la CONVENIENCIA PARA UN PROPÓSITO
PARTICULAR. Véase la Licencia Pública General de GNU para  más
detalles.

Debería  haber  recibido  una  copia  de  la  Licencia Pública
General junto con este programa. Si no ha sido así, escriba  a
la Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
Boston, MA  02110-1301  USA.  Añada también información  sobre
cómo contactar con usted mediante correo electrónico y postal.

Si el programa es interactivo, haga  que  muestre  un  pequeño
anuncio como el siguiente, cuando comienza a funcionar en modo
interactivo:

Gnomovision versión 69, Copyright (C) año   nombre  del  autor
Gnomovision no ofrece ABSOLUTAMENTE NINGUNA GARANTÍA. Para más
detalles escriba «show w».

Los comandos hipotéticos «show w» y «show c» deberían  mostrar
las  partes  adecuadas  de  la  Licencia  Pública General. Por
supuesto, los comandos que use pueden  llamarse  de  cualquier
otra  manera.  Podrían  incluso  ser  pulsaciones  del ratón o
elementos de un menú (lo que sea apropiado para su  programa).

También  debería  conseguir  que su empleador (si trabaja como
programador) o su  Universidad  (si  es  el  caso)  firme  una
«renuncia  de  copyright» para el programa, si es necesario. A
continuación se ofrece un ejemplo, altere  los  nombres  según
sea conveniente:

Yoyodyne,  Inc.  mediante  este documento renuncia a cualquier
interés de derechos de  copyright  con  respecto  al  programa
Gnomovision (que hace pasadas a compiladores) escrito por Pepe
Programador.

<firma de Pepito Grillo>,  20  de  diciembre  de  1996  Pepito
Grillo, Presidente de Asuntillos Varios.

Esta  Licencia  Pública  General  no  permite  que incluya sus
programas en programas propietarios. Si  su  programa  es  una
biblioteca   de  subrutinas,  puede  considerar  más  útil  el
permitir el  enlazado  de  aplicaciones  propietarias  con  la
biblioteca.  Si  este  es  el  caso,  use  la Licencia Pública
General de GNU para Bibliotecas en lugar de esta Licencia.

[QueryBox]
Cuadros de diálogo

En los cuadros de diálogo puede desplazarse con el teclado
usando las flechas o las teclas de las letras resaltadas.

También se pueden pulsar los botones con el ratón.

[How to use help]
Uso de la ayuda

Se pueden utilizar las flechas o el ratón para navegar
por el sistema de ayuda.

La flecha de abajo cambia al siguiente elemento o baja.
La tecla de arriba vuelve al elemento anterior o sube.
La tecla derecha sigue el enlace activo.
La tecla izquierda vuelve a la última página visitada.

Si el terminal no es compatible con las flechas de cursor
se puede avanzar con la barra espaciadora y retroceder con
la tecla b (back). El tabulador activa el elemento siguiente y
con INTRO se puede entrar al enlace correspondiente.
La tecla l (last) permite volver a la última página.

ESC pulsada dos veces permite salir de la ayuda.

El botón izquierdo del ratón avanza o sigue enlaces y el
botón derecho retrocede o vuelve a la última página.

La función de todas las teclas en la ayuda:

Las teclas de desplazamiento genéricasGeneral Movement Keys son válidas.

tabulador       Avanzar al elemento posterior.
Alt-tabulador   Retroceder al elemento anterior.
abajo           Avanzar elemento o bajar una línea.
arriba          Retroceder elemento o subir una línea.
derecha, INTRO  Seguir enlace.
izquierda, l    Volver a la última página visitada.
F1              Mostrar la ayuda del sistema de ayuda.
n               Pasar a la página siguiente.
p               Pasar a la página anterior.
c               Pasar a la página de contenidos.
F10, ESC        Salir de la ayuda.

Local variables:
fill-column: 58
end:
