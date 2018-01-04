# Script to generate inputfile to apply statistical potential in Rosetta given a set of constraints in the followting format OBSERVED RES1 CHAIN1 RESNUM1 RES2 CHAIN2 RESNUM2 ANYTHING (separeted for tab, otherwise edit line 12)
#run with python2.7 xl_generator.py
#PS. It just work with the zerolength, BS3/DSS and 1,6-hexanediamine. Does not work with short crosslinker propanediamine and BSG.

filename = raw_input("Provide the inputfile name: ")

file = open(filename, "r")

fh = open("xl", "w")

for line in file:
	line.rstrip()
	a,b,c,d,e,f,g,h=line.split("	")	
	if b=="LYS" and e=="LYS":
		fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " + "17.8 " + "-2.4989917608836549	-2.4989380291881389	-2.4988814339922101	-2.4988218226899335	-2.4987590345444914	-2.4986929002589022	-2.4986232414994447	-2.4985498704481870	-2.4984725892609276	-2.4983911895578785	-2.4983054518525023	-2.4982151449621597	-2.4981200253823772	-2.4980198366320110	-2.4979143085583928	-2.4978031566279242	-2.4976860811148072	-2.4975627663479827	-2.4974328798125498	-2.4972960712839267	-2.4971519718819764	-2.4970001930414583	-2.4968403255115845	-2.4966719382282463	-2.4964945771534985	-2.4963077640422853	-2.4961109951800609	-2.4959037399930821	-2.4956854396332346	-2.4954555054900993	-2.4952133175611380	-2.4949582228073268	-2.4946895333996508	-2.4944065248346305	-2.4941084340134694	-2.4937944571647677	-2.4934637476762873	-2.4931154138248530	-2.4927485163752863	-2.4923620660083543	-2.4919550207087013	-2.4915262829199492	-2.4910746965906583	-2.4905990440747701	-2.4900980428101320	-2.4895703419133497	-2.4890145184836001	-2.4884290738045820	-2.4878124292845314	-2.4871629222070624	-2.4864788012491772	-2.4857582217446179	-2.4849992407325772	-2.4841998117044568	-2.4833577790814161	-2.4824708724154334	-2.4815367002593121	-2.4805527437238197	-2.4795163496783061	-2.4784247235984367	-2.4772749220464902	-2.4760638447041856	-2.4747882260453480	-2.4734446265101724	-2.4720294232392916	-2.4705388003058033	-2.4689687384197896	-2.4673150041016925	-2.4655731382590602	-2.4637384441557515	-2.4618059747772350	-2.4597705194610171	-2.4576265898576821	-2.4553684051425080	-2.4529898764121754	-2.4504845902883972	-2.4478457915938634	-2.4450663651732611	-2.4421388166992983	-2.4390552524382656	-2.4358073580078781	-2.4323863759418600	-2.4287830820685485	-2.4249877606489463	-2.4209901781978260	-2.4167795558605576	-2.4123445403747610	-2.4076731734494388	-2.4027528595397598	-2.3975703318646993	-2.3921116166529828	-2.3863619954681781	-2.3803059655292600	-2.3739271978956822	-2.3672084934732993	-2.3601317366192234	-2.3526778463237861	-2.3448267247513286	-2.3365572030634212	-2.3278469843608036	-2.3186725835621473	-2.3090092640777584	-2.2988309711545298	-2.2881102616229327	-2.2768182299114414	-2.2649244301246654	-2.2523967939850991	-2.2392015443692799	-2.2253031042746443	-2.2106640009005787	-2.1952447646581277	-2.1790038227663899	-2.1618973871991329	-2.1438793366651225	-2.1249010922838352	-2.1049114866655145	-2.0838566259990330	-2.0616797447837598	-2.0383210528707423	-2.0137175743075204	-1.9878029776191397	-1.9605073970778903	-1.9317572443942481	-1.9014750104470295	-1.8695790564161143	-1.8359833938047814	-1.8005974527623039	-1.7633258380410552	-1.7240680719914963	-1.6827183238929138	-1.6391651248086418	-1.5932910673400329	-1.5449724893514940	-1.4940791408844234	-1.4404738333651039	-1.3840120700951957	-1.3245416571298847	-1.2619022934304667	-1.1959251392472652	-1.1264323614777823	-1.0532366549487051	-0.97614073811200797	-0.89493682205647929	-0.80940605119394604	-0.71931791424503899	-0.62442962394925416	-0.52448546374216676	-0.41921609978453489	0.00000000\n")
	elif b=="SER" and e=="SER":
                fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " +"13.4 " +"-2.4569439160586626	-2.4545985590921191	-2.4521768634876935	-2.4496763445476972	-2.4470944366967160	-2.4444284908640839	-2.4416757717517612	-2.4388334550421860	-2.4358986244878906	-2.4328682689283596	-2.4297392791959282	-2.4265084449361893	-2.4231724512956134	-2.4197278755400475	-2.4161711835367896	-2.4124987261238857	-2.4087067353739258	-2.4047913207268721	-2.4007484649937396	-2.3965740202493180	-2.3922637035557273	-2.3878130925986625	-2.3832176211162732	-2.3784725742425508	-2.3735730836633593	-2.3685141226178530	-2.3632905007416412	-2.3578968587535201	-2.3523276629493921	-2.3465771995270188	-2.3406395687270560	-2.3345086787867331	-2.3281782396807102	-2.3216417566727614	-2.3148925236710056	-2.3079236163266614	-2.3007278849345312	-2.2932979471279396	-2.2856261802680820	-2.2777047136605688	-2.2695254204572848	-2.2610799093381502	-2.2523595159054821	-2.2433552937873174	-2.2340580054733437	-2.2244581128379650	-2.2145457673614146	-2.2043108000270877	-2.1937427109023702	-2.1828306583574886	-2.1715634479660366	-2.1599295210198761	-2.1479169426656881	-2.1355133896940970	-2.1227061378740473	-2.1094820489433914	-2.0958275571010745	-2.0817286551264260	-2.0671708800146007	-2.0521392981409008	-2.0366184899612563	-2.0205925342015689	-2.0040449915395584	-1.9869588877554634	-1.9693166963334079	-1.9511003204897861	-1.9322910746450361	-1.9128696652514918	-1.8928161710373388	-1.8721100225848204	-1.8507299812499696	-1.8286541174038575	-1.8058597879607987	-1.7823236131789599	-1.7580214527024509	-1.7329283808339824	-1.7070186609980738	-1.6802657193784398	-1.6526421176877193	-1.6241195250750025	-1.5946686891002173	-1.5642594057753740	-1.5328604886362882	-1.5004397368029458	-1.4669639019994065	-1.4323986545241496	-1.3967085480890091	-1.3598569835321541	-1.3218061713614588	-1.2825170930518652	-1.2419494611294795	-1.2000616779223492	-1.1568107929979305	-1.1121524592090282	-1.0660408873172855	-1.0184287991451129	-0.96926737920875894	-0.91850622478523292	-0.86609329435486870	-0.81197485438133299	-0.75609542436177435	-0.69839772010345769	-0.63882259514139150	-0.57730898028785305	0.00000000\n")
	elif b=="GLU" and e=="GLU":
                fh.write("AtomPair " + "CB " + d +  " CB " + g + " ETABLE 3.0 " + "15.1 " + "-2.4684200489318755	-2.4683234450694727	-2.4682209345046431	-2.4681121560734027	-2.4679967265419691	-2.4678742392370623	-2.4677442626234551	-2.4676063387760223	-2.4674599817699345	-2.4673046759744466	-2.4671398742320889	-2.4669649959232629	-2.4667794249362487	-2.4665825074735039	-2.4663735497797461	-2.4661518156699458	-2.4659165239445429	-2.4656668456518673	-2.4654019011431956	-2.4651207569859253	-2.4648224226821185	-2.4645058471560333	-2.4641699150870409	-2.4638134429442289	-2.4634351748354675	-2.4630337780781701	-2.4626078385081200	-2.4621558554936200	-2.4616762366476905	-2.4611672922219441	-2.4606272291475761	-2.4600541447234718	-2.4594460199132300	-2.4588007122274576	-2.4581159481767827	-2.4573893152683013	-2.4566182534999825	-2.4558000463403005	-2.4549318111639877	-2.4540104890857037	-2.4530328342025314	-2.4519954021361627	-2.4508945379184297	-2.4497263630964881	-2.4484867620867590	-2.4471713676557556	-2.4457755455568986	-2.4442943781832582	-2.4427226472598704	-2.4410548154410208	-2.4392850068270491	-2.4374069862424221	-2.4354141372768936	-2.4332994389842497	-2.4310554411295016	-2.4286742379608768	-2.4261474403501779	-2.4234661462378426	-2.4206209092772042	-2.4176017055506236	-2.4143978982592671	-2.4109982002592005	-2.4073906342764531	-2.4035624907428428	-2.3995002830070007	-2.3951896998150914	-2.3906155549229879	-2.3857617335725081	-2.3806111357462214	-2.3751456159116060	-2.3693459191126749	-2.3631916131453181	-2.3566610165689781	-2.3497311223527504	-2.3423775168175780	-2.3345742936489842	-2.3262939626456500	-2.3175073528836947	-2.3081835099692398	-2.2982895870136417	-2.2877907289366703	-2.2766499497010955	-2.2648280020475795	-2.2522832392587588	-2.2389714684904902	-2.2248457951245655	-2.2098564576172066	-2.1939506522430747	-2.1770723471599922	-2.1591620850649633	-2.1401567738357699	-2.1199894643559674	-2.0985891147720395	-2.0758803403423371	-2.0517831480065070	-2.0262126547422667	-1.9990787887181796	-1.9702859721783170	-1.9397327849674184	-1.9073116075160215	-1.8729082419940823	-1.8364015103434213	-1.7976628277774580	-1.7565557502148295	-1.7129354940880148	-1.6666484268625936	-1.6175315263972152	-1.5654118073780410	-1.5101057126885280	-1.4514184676663717	-1.3891433949465863	-1.3230611875242175	-1.2529391374373517	-1.1785303174419823	-1.0995727127647115	-1.0157882999174035	-0.92688206935054041	-0.83254098854558833	-0.73243290190112020	-0.62620536362555868	-0.51348439948196756	0.00000000\n")
	elif b=="ASP" and e=="ASP":
                fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " +"13.5 " + "-2.4625863939945702	-2.4624837791307073	-2.4623737153669936	-2.4622556619797251	-2.4621290389986825	-2.4619932243476796	-2.4618475507995754	-2.4616913026839029	-2.4615237123871339	-2.4613439565691806	-2.4611511521216016	-2.4609443518456828	-2.4607225397630828	-2.4604846261536295	-2.4602294422002160	-2.4599557342335174	-2.4596621575765312	-2.4593472699561971	-2.4590095243765973	-2.4586472615701496	-2.4582587018121558	-2.4578419361896522	-2.4573949172081484	-2.4569154487653577	-2.4564011753172963	-2.4558495703531662	-2.4552579239498300	-2.4546233294677222	-2.4539426692754205	-2.4532125994301168	-2.4524295332521433	-2.4515896237026027	-2.4506887444840686	-2.4497224697661295	-2.4486860524521035	-2.4475744008377660	-2.4463820536329877	-2.4451031530952605	-2.4437314162605617	-2.4422601041005692	-2.4406819883879507	-2.4389893162042426	-2.4371737718356599	-2.4352264359404217	-2.4331377417183830	-2.4308974279156246	-2.4284944884166180	-2.4259171181693091	-2.4231526552030118	-2.4201875184226083	-2.4170071408771037	-2.4135958982114971	-2.4099370319127047	-2.4060125669893750	-2.4018032236381259	-2.3972883225796977	-2.3924456834283774	-2.3872515157745511	-2.3816803022818931	-2.3757046733626339	-2.3692952727142256	-2.3624206131207757	-2.3550469217807404	-2.3471379744078149	-2.3386549173046660	-2.3295560764672700	-2.3197967529486050	-2.3093290032338700	-2.2981014037904970	-2.2860587984578160	-2.2731420275486016	-2.2592876372618775	-2.2444275680281862	-2.2284888202229922	-2.2113930956584227	-2.1930564129979757	-2.1733886953334149	-2.1522933277847187	-2.1296666830385220	-2.1053976124421752	-2.0793669001650414	-2.0514466778186033	-2.0214997965304065	-1.9893791535214405	-1.9549269698291027	-1.9179740156214393	-1.8783387793446309	-1.8358265766109980	-1.7902285944364849	-1.7413208662183024	-1.6888631723595608	-1.6325978611785104	-1.5722485843689356	-1.5075189407762082	-1.4380910218569625	-1.3636238517538004	-1.2837517143088917	-1.1980823588673957	-1.1061950760849868	-1.0076386343680497	-0.90192906685842900	-0.78854729815793689	-0.66693659923112136	-0.53649985808806377	-0.39659665293584112	0.00000000\n")
	elif (b=="LYS" and e=="SER") or (b=="SER" and e=="LYS"):
		fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " + "15.8 " + "-2.4601752162088815	-2.4599347472139925	-2.4596822931598581	-2.4594172567049100	-2.4591390107379993	-2.4588468968977395	-2.4585402240008989	-2.4582182664198626	-2.4578802623582305	-2.4575254120609316	-2.4571528759042849	-2.4567617724133015	-2.4563511761989503	-2.4559201157208008	-2.4554675710533047	-2.4549924713974178	-2.4544936926286027	-2.4539700545537926	-2.4534203181901830	-2.4528431827857275	-2.4522372827668732	-2.4516011845007597	-2.4509333828973467	-2.4502322978478333	-2.4494962705030048	-2.4487235593333025	-2.4479123360069934	-2.4470606810646132	-2.4461665793896827	-2.4452279154284042	-2.4442424681874400	-2.4432079059770331	-2.4421217809031077	-2.4409815230610548	-2.4397844344639452	-2.4385276826578774	-2.4372082940244582	-2.4358231467376754	-2.4343689633678878	-2.4328423031620332	-2.4312395538654528	-2.4295569231835543	-2.4277904298360227	-2.4259358941053506	-2.4239889279488125	-2.4219449246302247	-2.4197990478351130	-2.4175462201783375	-2.4151811112424184	-2.4126981249355595	-2.4100913862639572	-2.4073547274128941	-2.4044816731984611	-2.4014654256898211	-2.3982988481620851	-2.3949744482051756	-2.3914843599850428	-2.3878203256572306	-2.3839736757981882	-2.3799353089125361	-2.3756956699144212	-2.3712447274774604	-2.3665719503514993	-2.3616662823988008	-2.3565161164769961	-2.3511092669650679	-2.3454329409250931	-2.3394737078269827	-2.3332174678107549	-2.3266494183008035	-2.3197540189830761	-2.3125149550578499	-2.3049150986335007	-2.2969364682066953	-2.2885601861162286	-2.2797664338977484	-2.2705344053938461	-2.2608422575322038	-2.2506670586408291	-2.2399847342348949	-2.2287700100314396	-2.2169963521773752	-2.2046359044798010	-2.1916594225040171	-2.1780362044228241	-2.1637340183624474	-2.1487190261832438	-2.1329557034187019	-2.1164067552745109	-2.0990330283930234	-2.0807934182630561	-2.0616447719876305	-2.0415417862204777	-2.0204369000311999	-1.9982801824044145	-1.9750192141800653	-1.9505989640456391	-1.9249616584202158	-1.8980466448301740	-1.8697902484782389	-1.8401256216529873	-1.8089825857023243	-1.7762874650397862	-1.7419629129908571	-1.7059277288899466	-1.6680966660933336	-1.6283802304642450	-1.5866844687734556	-1.5429107466115966	-1.4969555152238172	-1.4487100667392951	-1.3980602772244310	-1.3448863369485480	-1.2890624672181730	-1.2304566231396166	-1.1689301815749786	-1.1043376135567087	-1.0365261404622288	-0.96533537303912453	-0.89059693246599636	-0.81213405262315064	-0.72976116252539214	-0.64328344802561332	-0.55249639173416654	-0.45718529004079755	-0.35712474615866086	-0.25207813793167588	-0.14179705925926100	0.00000000\n")
	elif (b=="GLU" and e=="ASP") or (b=="ASP" and e=="GLU"):
		fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0" + " 14.3 " + "-2.4838569045659824	-2.4836266624151904	-2.4833836251400498	-2.4831270816794131	-2.4828562814655015	-2.4825704322192905	-2.4822686976222030	-2.4819501948913967	-2.4816139921840659	-2.4812591058635007	-2.4808844976396358	-2.4804890715204237	-2.4800716706067760	-2.4796310737037857	-2.4791659917573270	-2.4786750640778337	-2.4781568543548929	-2.4776098464626557	-2.4770324400178652	-2.4764229457050533	-2.4757795803288900	-2.4751004615900456	-2.4743836025991186	-2.4736269060449558	-2.4728281580610201	-2.4719850217552448	-2.4710950303742720	-2.4701555800747883	-2.4691639223165112	-2.4681171558186179	-2.4670122180668841	-2.4658458763678937	-2.4646147183666471	-2.4633151420948707	-2.4619433453972306	-2.4604953148482309	-2.4589668139706191	-2.4573533708771720	-2.4556502651539631	-2.4538525140851561	-2.4519548580428818	-2.4499517451276915	-2.4478373149086110	-2.4456053812809841	-2.4432494143802614	-2.4407625214662403	-2.4381374267668434	-2.4353664501868479	-2.4324414848379092	-2.4293539733425860	-2.4260948827686661	-2.4226546782410878	-2.4190232950113568	-2.4151901090408501	-2.4111439059142867	-2.4068728480342543	-2.4023644399876503	-2.3976054920076422	-2.3925820813692553	-2.3872795116822090	-2.3816822698954638	-2.3757739809116174	-2.3695373596947320	-2.3629541607115243	-2.3560051245585782	-2.3486699216337001	-2.3409270926604222	-2.3327539859383251	-2.3241266910736158	-2.3150199690553563	-2.3054071784335974	-2.2952601973956916	-2.2845493415316014	-2.2732432769989828	-2.2613089289006894	-2.2487113845545537	-2.2354137913916929	-2.2213772491741111	-2.2065606962714810	-2.1909207895459986	-2.1744117776506755	-2.1569853672226600	-2.1385905816950981	-2.1191736122273142	-2.0986776604149782	-2.0770427722000022	-2.0542056626127305	-2.0300995307534322	-2.0046538645256078	-1.9777942345263000	-1.9494420764567622	-1.9195144615387107	-1.8879238541012455	-1.8545778557872836	-1.8193789355082117	-1.7822241444628162	-1.7430048153346434	-1.7016062447655713	-1.6579073582797719	-1.6117803565739450	-1.5630903422243136	-1.5116949256698717	-1.4574438093768549	-1.4001783489347872	-1.3397310898326396	-1.2759252785617718	-1.2085743466341228	-1.1374813660113432	-1.0624384743805422	-0.98322626858680451	-0.89961316448352591	-0.81135472136884346	-0.71819292899817810	0.00000000\n")
	elif (b=="LYS" and e=="ASP") or (b=="ASP" and e=="LYS"):
		fh.write("AtomPair " + "CB " + d + " CB " + g +  " ETABLE 3.0 " + "9.7 " + "-2.4881411414389731	-2.4880386937911680	-2.4879240258233040	-2.4877956798645755	-2.4876520243524283	-2.4874912331106316	-2.4873112621316977	-2.4871098235889804	-2.4868843567583099	-2.4866319954653591	-2.4863495316421904	-2.4860333745582466	-2.4856795051709923	-2.4852834250232263	-2.4848400990795199	-2.4843438917014282	-2.4837884950120497	-2.4831668487204297	-2.4824710503507958	-2.4816922548070579	-2.4808205619119690	-2.4798448905821715	-2.4787528379383730	-2.4775305216498964	-2.4761624034781562	-2.4746310917325900	-2.4729171201979625	-2.4709987006954179	-2.4688514460867736	-2.4664480603059928	-2.4637579913469381	-2.4607470429145906	-2.4573769397302385	-2.4536048409936484	-2.4493827958121983	-2.4446571336866327	-2.4393677822845348	-2.4334475038485834	-2.4268210405462014	-2.4194041578557517	-2.4111025739130127	-2.4018107611045707	-2.3914106047868700	-2.3797699020324217	-2.3667406813383423	-2.3521573219641141	-2.3358344490025047	-2.3175645774445002	-2.2971154753431620	-2.2742272125669842	-2.2486088576824841	-2.2199347810346808	-2.1878405171300983	-2.1519181337553164	-2.1117110491632047	-2.0667082315103471	-2.0163377070402930	-1.9599592947033670	-1.8968564751376107	-1.8262272910269530	-1.7471741635799845	-1.6586924962812191	-1.5596579217435647	-1.4488120303831238	-1.3247464007090457	-1.1858847295134183	-1.0304628366320685	0.00000000\n")
	elif (b=="LYS" and e=="GLU") or (b=="GLU" and e=="LYS"):
                fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " + "10.5 " + "-2.4716274357870134	-2.4715827018535492	-2.4715325967008539	-2.4714764754044154	-2.4714136155998858	-2.4713432081971405	-2.4712643469483737	-2.4711760167992907	-2.4710770808178495	-2.4709662655568536	-2.4708421446666762	-2.4707031205325620	-2.4705474037236854	-2.4703729899392783	-2.4701776342317316	-2.4699588220992155	-2.4697137371167628	-2.4694392247001815	-2.4691317514880211	-2.4687873598722945	-2.4684016170522227	-2.4679695579779946	-2.4674856214496685	-2.4669435785363021	-2.4663364523948985	-2.4656564284796332	-2.4648947539517394	-2.4640416250240378	-2.4630860607667273	-2.4620157617882796	-2.4608169519033254	-2.4594742008466710	-2.4579702256414748	-2.4562856681695848	-2.4543988460118271	-2.4522854733713757	-2.4499183484949754	-2.4472670035738702	-2.4442973125951539	-2.4409710521304078	-2.4372454093718261	-2.4330724311257654	-2.4283984066387347	-2.4231631763504993	-2.4172993576212320	-2.4107314775683335	-2.4033750017424609	-2.3951352462408977	-2.3859061592229409	-2.3755689561512554	-2.3639905912259565	-2.3510220453463262	-2.3364964085994870	-2.3202267325814319	-2.3020036250018165	-2.2815925556406000	-2.2587308389847749	-2.2331242548625596	-2.2044432636157580	-2.1723187672105269	-2.1363373619042250	-2.0960360214849061	-2.0508961429422925	-2.0003368781399331	-1.9437076660760795	-1.8802798700126004	-1.8092374124025810	-1.7296662877724884	-1.6405428194484557	-1.5407205100818828	-1.4289153180652647	-1.3036891721076245	-1.1634315138853708	-1.0063386339752469	-0.83039053844549926	0.00000000\n")
	elif (b=="ASP" and e=="SER") or (b=="SER" and e=="ASP"):
                fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " + "7.0 " + "-2.4496999923612748	-2.4485597391758347	-2.4472413797957415	-2.4457170942732773	-2.4439547172369203	-2.4419170591463626	-2.4395611215295503	-2.4368371896489407	-2.4336877834430197	-2.4300464445987018	-2.4258363342160010	-2.4209686113936186	-2.4153405585784640	-2.4088334141306404	-2.4013098663272103	-2.3926111560140271	-2.3825537266930041	-2.3709253514280135	-2.3574806548640481	-2.3419359358704241	-2.3239631816686597	-2.3031831470798352	-2.2791573530848837	-2.2513788358446618	-2.2192614511732245	-2.1821275089678238	-2.1391934769562795	-2.0895534523588140	-2.0321600533206947	-1.9658023274314473	-1.8890802120658918	-1.8003750087809749	-1.6978152503797901	-1.5792372422874905	-1.4421394485980272	-1.2836297638568794	-1.1003645630044048	-0.88847825000993907	-0.64350182748239604	-0.36026878096890869	0.00000000\n")
	elif (b=="GLU" and e=="SER") or (b=="SER" and e=="GLU"):
                fh.write("AtomPair " + "CB " + d + " CB " + g + " ETABLE 3.0 " +"7.7 " + "-2.4731055413267313	-2.4722369910050475	-2.4712590225281019	-2.4701578516524023	-2.4689179576398601	-2.4675218644897541	-2.4659498946311942	-2.4641798915799882	-2.4621869076563598	-2.4599428523615643	-2.4574160964712064	-2.4545710262373177	-2.4513675414600584	-2.4477604903004249	-2.4436990329340915	-2.4391259250132862	-2.4339767109031527	-2.4281788152729860	-2.4216505202730332	-2.4142998138868279	-2.4060230932191189	-2.3967037044676545	-2.3862102990078711	-2.3743949824347510	-2.3610912304920930	-2.3461115425598109	-2.3292447996354895	-2.3102532896264165	-2.2888693580862309	-2.2647916372534382	-2.2376808003173210	-2.2071547812138306	-2.1727833926888707	-2.1340822669662884	-2.0905060338391195	-2.0414406403488101	-1.9861947041354142	-1.9239897790776013	-1.8539493966218288	-1.7750867290851602	-1.6862907019931299	-1.5863103609881364	-1.4737372744184540	-1.3469857256022806	-1.2042704180294095	-1.0435813824024081	-0.86265573583841615	0.00000000\n")
	else:
		print "NOT FOUND", d, g

fh.close()
file.close()