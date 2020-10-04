def getIcon(icon, react=False):
    """
        Bank
        Extract
        Transfer
        Name
        ID
        Money
        Receiver
        Wallet
        Atm
        Rank
        Deposit

        Casanik
        Ghost
        Thriller
        Conffeti
        Win
        Frank
        Jack

        Identity
        Language
        Storage
        Website
        Calendar
        Design
        HD
        Imac

        Play
        Pause
        Shuffle
        Playlist
        Sound
        Audio Wave
        Audio Wave Error
        Audio Wave Warning
        Time
        Love Music
        DJ
        User
        Live

        Covid 19
        Covid Cases Actives
        Covid Cases Recovered
        Covid Cases Fatal
        Covid News
        
        Store
        Store Error
        Weapons Store
        Weapons Store Error
        Close
        Back
        M4A1
        AK47
        M1911
        GLOCK
        Image

        Discord
        Activity
        Color Picker
        Status
        About
        Png
        Gif
        Calendar
        Inventory
        Chat
        Photo
        Chat Message
        Chat Voice
        Location
        Counter
        Padlock locked
        Padlock unlocked
        Pica Pau
        Owner
        Profile Resume
        Members

    """
    IconsList = {
        "Transfer": "<:transferencia:708796560594436146>",
        "Receiver": "<:destinatario:708792474872840273>",
        "Atm": "<:caixaeletronico:708796560640835705>",
        "Deposit": "<:deposito:708805001383903252>",
        "Extract": "<:extrato:708796560628252672>",
        "Wallet": "<:carteira:708796560602955786>",
        "Money": "<:dinheiro:708796560607019129>",
        "Bank": "<:banco:708798644723122287>",
        "Name": "<:nome:708792474856062996>",
        "Rank": "<:rank:708800563927711874>",
        "ID": "<:id:708792474629308530>",

        "Casanik":"<:caca_niqueis:708824350106714174>",
        "Thriller":"<:caveira:708824350098325596>",
        "Conffeti":"<:confete:708824350450778202>",
        "Ghost":"<:fantasma:708824350425350225>",
        "Frank":"<:frank:708824350404509736>",
        "Win":"<:ganhou:708824350278549575>",
        "Jack":"<:jack:708824350387732550>",

        "Storage":"<:armazenamento:708828994052816967>",
        "Calendar":"<:calendario:708828993859616830>",
        "Website":"<:website:708828994249949276>",
        "Language":"<:lingua:708828994224652410>",
        "Identity":"<:design:708828994153349162>",
        "Design":"<:design:708828994153349162> ",
        "Imac":"<:imac:708828993755021373>",
        "HD":"<:hd:708828994090565682>",

        "Audio Wave Warning":"<:ondas_de_audio_aviso:709140014805549169>",
        "Audio Wave Error":"<:ondas_de_audio_erro:709140014705147977>",
        "Audio Wave":"<:ondas_de_audio:709140014855880706>",
        "Playlist":"<:lista_de_musica:709140014755217450>",
        "Volume Down":"<:volume_baixo:709173506281177168>",
        "Volume Up":"<:volume_alto:709173506214199327>",
        "Love Music":"<:amo_musica:709140015132704840>",
        "Shuffle":"<:aleatorio:709174331426603069>",
        "Pause":"<:pausar:709174404986306562>",
        "User":"<:usuario:709140014776451186>",
        "Live":"<:ao_vivo:709140014746959977>",
        "Next":"<:proxima:709173506281308230>",
        "Time":"<:tempo:709140015145549883>",
        "Stop":"<:parar:709173505983250553>",
        "Play":"<:play:709173505832386632>",
        "Sound":"<:som:709140015262728373>",
        "DJ":"<:DJ:709140014847492138>",

        "Covid 19":"<:covid19:714154900355022849>",
        "Covid Cases Actives":"<:ativos:714154900489240627>",
        "Covid Cases Recovered":"<:recuperados:714154900396834856>",
        "Covid Cases Fatal":"<:morto:714154900384120843>",
        "Covid News":"<:news:714205869801209937>",
        
        "Store":"<:Loja:722881797871894609>",
        "Store Error":"<:Loja_Erro:722881798035472499>",
        "Weapons Store":"<:Loja_de_Armas:722876394857693204>",
        "Weapons Store Error":"<:Loja_de_Armas_Erro:722881798476136518>",
        "Close":"<:Fechar:722879987220217866>",
        "Back":"<:Voltar:722879813786009691>",
        "M4A1":"<:M4A1:722876394891116675>",
        "AK47":"<:AK47:722879813756387568>",
        "M1911":"<:M1911:722876394819944528>",
        "GLOCK":"<:GLOCK:722876394870407241>",
        "Image":"<:image:722885601392721931>",

        "Discord":"<:discord:723083219582582825>",
        "Activity":"<:atividade:723083219758743573>",
        "Color Picker":"<:conta_gotas_cor:723083219594903565>",
        "Status":"<:status:723083219636846665>",
        "About":"<:sobre:723083219423199273>",
        "Png":"<:png:723088641550843904>",
        "Gif":"<:gif:723088641525809152>",
        "Calendar":"<:calendario:723088568322490368>",
        "Inventory":"<:inventario:723088641580335134>",
        "Chat":"<:chat:723088568326684704>",
        "Photo":"<:foto:723088641538392104>",
        "Chat Message":"<:chat_mensagem:723092264343175268>",
        "Chat Voice":"<:voz:723092263885864992>",
        "Location":"<:localizacao:723092264066220113>",
        "Counter":"<:contador:723092264011825174>",
        "Padlock locked":"<:cadeado:723090988473778226>",
        "Padlock unlocked":"<:cadeado_desbloqueado:723090988117262337>",
        "Pica Pau":"<:pica_pau:723090988616384633>",
        "Owner":"<:dono:723090988582699039>",
        "Profile Resume":"<:resumo_perfil:723096976740319243>",
        "Members":"<:membros:723096976765354084>",

        "Module":"<:modulo:725758847918276820>",
        "Module Warning":"<:modulo_aviso:725758847683133452>",
        "Module Error":"<:modulo_erro:725758847775408261>",
   }

    if react is True:
        return IconsList[icon].replace("<", "").replace(">", "")

    return IconsList[icon]
