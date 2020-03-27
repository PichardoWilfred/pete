@ECHO OFF

:: That's an input
SET /P comando= esbria

REM that's Add.bat 
IF %comando%== add (

 python add.py %* 

REM that's el.bat 
) ELSE IF %comando% == el (

 python el.py %* 

REM that's help.txt
) ELSE IF %comando% == helpp ( 

MORE help.txt 


) ELSE IF %comando% == hor ( 

TYPE horario.txt 

REM that's new.bat 
) ELSE IF %comando% == new ( 

python new.py %1 

REM that's open.bat
) ELSE IF %comando% == open ( 
 
python open.py %* 

REM that's show.bat 
) ELSE IF %comando% == test ( 

ECHO has escrito test

) ELSE IF %comando% == show ( 

python show.py

) ELSE ( 

TYPE help.txt

)

:: That was easy modo foka





















