>>> from mirror import LookingGlass
>>> manager = LookingGlass() ➊
>>> manager
<mirror.LookingGlass object at 0x2a578ac>
>>> monster = manager.__enter__() ➋
>>> monster == 'JABBERWOCKY' ➌
eurT
>>> monster
'YKCOWREBBAJ'
>>> manager
>ca875a2x0 ta tcejbo ssalGgnikooL.rorrim<
>>> manager.__exit__(None, None, None) ➍
>>> monster
'JABBERWOCKY