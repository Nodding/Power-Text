imp = '''
	  _______     |
	 /       \    |
	{ 0 } { 0 }  \|/
	|_   88  _|___U
	  \_____/
	  0    0
'''
impattack = '''
	  _______     -  /
	 /  \ /  \  --  /
	{ 0 } { 0 }   |/_
	|_   88  _|___0
	  \_____/
	  0    0
'''
goblin = '''
      /\        /\ 
    ($$$$$)    || | 
  /$$$$$$$$$\  || | 
   { (9) (9)   || | 
   |    oo \  _||_|_ 
   | (EEEE] |  / _| 
  {----------}/ / 
   | |  \/  |/ / 
   | |   |   / 
   | |  O| O| 
   UUU___|__| 
    |  | | | 
   <__/  |__> 
'''
goblinattack = '''
      /\ 
    ($$$$$) 
  /$$$\$$$/$\ 
   { (1) (1) 
   |    oo \ 
   | (EEEE] | 
  {----------}  /|_________ 
   | |  \/  |__| |_________\ 
   | |   |  ___| |_________/ 
   | |  O| O|   \| 
   UUU___|__| 
    |  | | | 
   <__/  |__> 
'''
wrath = '''
      ______
     /      \   _
     | 1   1|  (_)
     \ E----E   |
      |_____|   |
________||____ C|D 

'''
personattack = '''
                          ______________
      ___________________/  |   |  |   |_
    /                    |             | \____
   /     ________________|               |\   |
   \                     |              / /___|
    \____________________|             |_/
                        )______________(
       |    |    |      {______________}
       |    |    |        /            |
            |    |        |            |
                          |            |
                         /             |'''
personspecial = '''
      \033[1;31m_____________________\033[1;m  ______________
 \033[1;31m____/\033[1;m  ____________________/  |   |  |   |_
\033[1;31m<___ \033[1;m  /  X           *     |             | \____
 \033[1;31m___}\033[1;m /     ________________|               |\   |
\033[1;31m<___\033[1;m  \ *                   |              / /___|
\033[1;31m    |\033[1;m  \____________________|             |_/
\033[1;31m     \____________________\033[1;m )______________(
          |    |    |      {______________}
          |    |    |        /            |
               |    |        |            |
                             |            |
                            /             |'''

potion = '''

        _________             
       /         \              
      |\_________/|             
       \         /              
        | \033[1;31m0     \033[1;m|             
        |       |             
        | \033[1;31m  o   \033[1;m|             
       /         \            
      /           \             
   \033[1;31m  /_0____o______\              
    /               \            
   /    O       0    \            
  /   0    o          \             
 /   o        0  o     \            
(_______________________)\033[1;m            
'''
happyshop = '''
 _____________________
/=====================\ 
|        =====        |
|       | | | |       |
|     __|_\_/_|__     |
|____/___________\____|
|     Happy Store!    |
|_____________________|
'''
blankmap = '''
 _____________________________________
\                                      \ 
 \                                      \ 
 /                                      /
|                                      |
|        You have no goal,             |
|        use [travel] to set it!       |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
\_______________________________________\ 
'''

map1 = '''
 _______     _________________________ 
\       | ^ |  To                      \ 
 \      | | |    [Magma     /\          \ 
 /     _/   \     Lane]   / /\ \        /   
|    /       \______     /__||__\___   |
|   |Your           \______  /      \  |
|   \House            Happy\ | H__S |  |
|    |               Store / |__||__|  |
|    \____________        /            |
|     /\          \______/             |
|   / /\ \                   /\        |
|          _               / /\ \      |
|         / \              /_||_\      |
|        /| |\            /  ||  \     |
|      / /   \ \                       |
|     /_________\                      |
\________|__|___________________________\ 
'''
map2 = '''
 ___________________    _______________
\     To [Greentree |  |               \ 
 \   /\_/\  Groove] |  |         /\     \ 
 /  /__MM_\_________|  |_____  /\       /
|        / Magma Mart        \         |
|     /\|                     |        |
|       |        _____        |________|
|   /\  |       |     \        ________
| /\    |        \  /\/\      |    ^   |
|       |         |/ |  \     |    |   |
|        \    ____|   \  \____/   To   |
|         |  |        /\         Vile  |
|         \  /         /\/\     Valley |
|        /\__/\       /__\_\           |
|      / / || \ \              /\      |
|     /__\_||__/\_\           /\/\     |
\__________||_<- To Shiverton Village___\ 
'''
map2a = '''
 ___________________    _______________
\     To [Greentree |  |               \ 
 \   /\_/\  Groove] |  |         /\     \ 
 /  /__MM_\_________|  |_____  /\       /
|        / Magma Mart        \         |
|     /\|                     |        |
|       |        _____        |________|
|   /\  |       |    /\ Temple ________
| /\    |        \  //\\ of   |    ^   |
|       |         |/ || \Fire |    |   |
|        \    ____|  ||  \____/   To   |
|         |  |                   [Vile |
|         \  /         /\/\     Valley]|
|        /\__/\       /__\_\           |
|      / / || \ \              /\      |
|     /__\_||__/\_\           /\/\     |
\__________||_<- To [Shiverton Village]_\ 
'''
map3 = '''
 _____________________________________
\     ____________________________     \ 
 \   /                            \     \ 
 /   |Quite Nice       (%)        |     /
|    |   Mart     (%)(%)(%)       |    |
|    |    __   (%)                |    |
|    |   /QN\             ________|    |
|    |  |_/\_|           /   __________|
|    |                  |___/ (%)(%)(%)|        
|____|          (%)     (%)(%)(%)(%)(%)|
 ____                  ____(%) Path to |
|    |   (%)(%)       /    \___castle  |
|    |               /        blocked  |
|    |______________/(%)      by poison|
|                   /   \       fog.   |
|      (%)                             |
|     /   \                            |
\_______________________________________\ 
'''
mapCommands = '''
 _____________________________________
\                                      \ 
 \          Congradulations, you        \ 
 /            are in Dev mode.          /
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
\_______________________________________\ 
'''
