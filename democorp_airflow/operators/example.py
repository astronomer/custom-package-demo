from airflow.models import BaseOperator
from airflow.utils.context import Context


class ExampleOperator(BaseOperator):
    """
    This operator prints an ASCII art Airflow logo as an example.

    Example usage:
    ```
    from democorp_airflow.operators.example import ExampleOperator

    mytask = ExampleOperator(task_id="mytask")
    ```
    """

    def execute(self, context: Context) -> None:
        # ASCII logo generated using
        # https://icon-icons.com/icon/apache-airflow-logo/145494
        # and https://ascii-generator.site
        airflow_logo = """
*@@@@@@@%%%%##***++==--::.                                                           :#@%=
#@@@%*****####%%%@@@@@@@@@@@@%#*+-:.                                               :#@@@@@
 -%@@#-               ..:-==+*#%@@@@@#*=:                                        :#@@%-@@@
   -#@@%-                        .:=*%@@@@#=.                                  :#@@%-  @@@
     -%@@%-                            :=#@@@%=                              .*@@@=    @@%
       :#@@%-                              -*@@@+.                         .*@@%=     .@@#
         :#@@%-                               +@@@*.                     .+@@@=       :@@*
           :*@@%=                              :%@@@*.                 .*@@%=         -@@+
             .*@@@=                              %@@@@#:             .+@@@=           +@@=
               :*@@@=                            =@@#@@@#:          +@@@=             #@@:
                 .*@@%=                          .@@# =%@@#:      +@@@=               @@@ 
                   .+@@@+                         @@@   -%@@#:  +@@@+                .@@% 
                     .*@@@+:--:                  .@@@     -%@@#@@@+                  =@@* 
                       .#@@@@@@@#+.              -@@#       -%@@@.                   #@@- 
                      .*@@@= .=#@@@#:            *@@=         @@@                    @@@  
                    .*@@%=      .=@@@#:         .@@@        .%@@=                   =@@*  
                  .*@@@=           =@@@*        #@@-       -@@@=                    @@@.  
                .+@@@=              .#@@%:     -@@#      -#@@%:                    +@@*   
              .*@@@*-------:.         -@@@+   .@@@.   .=%@@%-                     -@@%    
             +@@@@@@@@@@@@@@@@@%#+=:   .%@@*  #@@- .=%@@@#-                      .@@@:    
           +@@@@#+-:......:-=+*#@@@@@%*=-@@@%@@@%+%@@@%=.                        %@@=     
         =@@@*-                   :-+#%@@@@@#*%@@@@#=.                         :@@@=      
       .#@@#.                           *@@+  .@@@                            +@@@:       
      :%@@=                          -+%@@@@#*@@@@@%*=-.                   .+@@@*         
     :@@@:                        -*@@@@*#@@@%@@@++#@@@@@%#+=-:.      .:=+%@@@*.          
     %@@-                      .+@@@@*: .@@@. +@@@:  .:=*#@@@@@@@@@@@@@@@@@@#.            
    *@@+                     .*@@@*-    %@@-   =@@@=        .:--=====-+@@@#:              
   -@@%                    .*@@@=      +@@*     .%@@#.              -%@@#:                
   %@@:                   :@@@+       .@@@        *@@@=           :#@@%-                  
  -@@*                   :@@@:        #@@-         :#@@%=       :#@@%-                    
  #@@:                   #@@:        :@@%            :#@@@*-  :#@@%-                      
 .@@@                    #@@%-       +@@+              .+%@@@@@@@%.                       
 =@@*                  =@@@%@@%-     #@@:                  :===+@@@+.                     
 *@@-                =@@@*. :*@@%-   #@@.                        +@@@+.                   
 %@@.              =%@@*.     :*@@%= +@@:                         .+@@@*.                 
.@@@             -%@@*.         .*@@@*@@+                            =@@@*.               
:@@#           -%@@#:             :#@@@@@.                             =@@@*.             
=@@*         :%@@#:                 :#@@@@:                              =%@@*:           
*@@+       -%@@#:                     .*@@@+                               =@@@#:         
#@@=     :#@@%:                         .+@@@*:                              =%@@#:       
%@@-   :%@@%-                              =%@@@*=.                            -%@@%-     
%@@: :#@@%-                                  .=#@@@@#+-:                         -%@@#-   
@@@=#@@%-                                        :=*%@@@@@%#++=-:..                -#@@%- 
@@@@@%-                                               .:=+*%@@@@@@@@@@@%%###****+++++%@@@#
=%@#=                                                         ..:--=++***###%%%%@@@@@@@@@=
"""
        print(airflow_logo)
