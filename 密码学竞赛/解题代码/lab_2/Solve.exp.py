from z3 import *
from Crypto.Util.number import *
a=Int('a')
b=Int('b')
c=Int('c')
d=Int('d')
n=Int('n')
s=Solver()
s.add(n==25984447105840144204726140518647900810784318911045573112702803720063269869257246042781455515220370300371322369266627365164963900956417121636243251367488604111626434846517930558172038293909575081418247263246677965935401509016648320330056450224647570170228839618324017216433438353329486961004973591440745242575179169717586964468085738007027674627155651009822600433194871839925969830314107920656674510625530946074904257516348409397307237681561961003851975377309117862295975361599123005804187055793580478466920231809749203892985196997737336922757484520071802590727361629983940666693096733397198360027049521098899469448853)
s.add((a * (60002354876251355965151562461247480482515496917741490298630771974220930616675 ** 3%n) + b * (60002354876251355965151562461247480482515496917741490298630771974220930616675 ** 2%n) + c *60002354876251355965151562461247480482515496917741490298630771974220930616675 + d) ==14181596274179526270805648290965819183528910754084659334605288823011431923494810964618766383224468657336083499258652848323435316206518871238278390527952953233408140711018765090665412398441127680243810022418572215280840348762490378846576762238657647443827970992465977448622826233543588521900433003381689305190)
s.add((a * (58317991346743938885993146146362677289105991977049568233220781228102038659484 ** 3 %n)+ b * (58317991346743938885993146146362677289105991977049568233220781228102038659484 ** 2 %n)+ c * 58317991346743938885993146146362677289105991977049568233220781228102038659484+ d) ==13020507237617729101718169310293495896780990322849291274557306869164121907152343623103434927547806240534514353324680741670730400192907493220067190327715636790469225408448798957817955019606110374482663353526138246279563848414962592714024348009716085769623595857071669185084613855032160704801649492912935317281)
s.add((a * (109801116737516263821905127008163207467616293313761078189248696049962628110949 ** 3%n) + b *( 109801116737516263821905127008163207467616293313761078189248696049962628110949 ** 2%n) + c * 109801116737516263821905127008163207467616293313761078189248696049962628110949 + d) ==86904147451931807955533431713083983944972076149471934932594655101733780670944036591700055783164601235570340269628067942075097931238498118411256150059286615793580571727917569247675631324066425438239734529864493547038967164455855057637662611807397083364424800853855512915617156269333736827491103562091873714726)
s.add((a * (109520698511811251058487504853775804612539348423792492555579233854741004839310 ** 3%n) + b *( 109520698511811251058487504853775804612539348423792492555579233854741004839310 ** 2%n )+ c * 109520698511811251058487504853775804612539348423792492555579233854741004839310 + d) ==86240019693849224437564934457396859854220939969432917244576569005011506620714157380158981500421291449351366433310370141191675695372289703300696385884236633200503092443813042966281339361996433319009234365291250050889452052769388812530848281725044074009032309997114549110114740708601370953679197280682793278275)
if s.check()==sat:
	print('have result')
	res=s.model()
	print(res)
else:
	print('no result')
#d = 56006392793403656735538704089732107703878971419442672690342926545436898285415526975954922123503952765
x=56006392793403656735538704089732107703878971419442672690342926545436898285415526975954922123503952765
print(long_to_bytes(x))