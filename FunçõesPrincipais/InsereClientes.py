from Interface.CriaPerguntas import *
from VerificaçõesDeDados.VerificaçõesEntrada import *
from FunçõesPrincipais.DefineId import *
from Interface.MostraEstoqueDisponivel import *
from FunçõesPrincipais.ValoresProdutos import *
from datetime import date
from Interface.MostraMensagem import *
from VerificaçõesDeDados.VerificaçõesEstoque import *
from tinydb import Query
from customtkinter import CTk, CTkScrollableFrame

Cliente = Query()

def insereClientes(interface):
    interface.withdraw()
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    interfaceUsuario = CTkToplevel()
    interfaceUsuario.title("Gerenciador de Dados - LH Locações")
    interfaceUsuario.geometry("1400x700")#765x880
    interfaceUsuario.configure(fg_color=corInterfacePrincipal)

    tituloPrincipal = CTkLabel(interfaceUsuario, text="Cadastro de Clientes", font=("roboto", 24, "bold"), text_color=corFonte)
    tituloPrincipal.grid(row=0, column=0)

    framePrincipal = CTkFrame(interfaceUsuario, width=840, height=660, fg_color=corFundoFrame, border_color=corBordas, corner_radius=15, border_width=2)
    framePrincipal.grid(row=1, column=0, pady=20, padx=40)

    criaBotao(interfaceUsuario, "Cadastrar Cliente", lambda: confirmaContrato(janelasCadastro.tab("Cliente"), framePrincipal), 3, 0)

    janelasCadastro = CTkTabview(framePrincipal, width=600, height=630, border_color=corBordas, border_width=2, fg_color=corBotao, text_color="white", segmented_button_selected_color=corFundoFrame, segmented_button_fg_color=corBordas)
    janelasCadastro.grid(row=0, padx=20, pady=30)
    janelasCadastro.add("Cliente")
    janelasCadastro.add("Produtos")
    janelasCadastro.add("Preços")
    janelasCadastro.add("Tamanhos")

    # Tornar a janela principal responsiva
    interfaceUsuario.grid_columnconfigure(0, weight=1)  # Configura a coluna 0 da janela principal
    interfaceUsuario.grid_rowconfigure(1, weight=1)    # Configura a linha 1 da janela principal

    # Tornar o framePrincipal responsivo
    framePrincipal.grid_columnconfigure(0, weight=1)   # Configura a coluna 0 do frame principal
    framePrincipal.grid_rowconfigure(0, weight=1)      # Configura a linha 0 do frame principal

    # Tornar as abas do janelasCadastro responsivas
    janelasCadastro.grid_columnconfigure(0, weight=1)  # Configura a coluna dentro da aba
    janelasCadastro.grid_rowconfigure(0, weight=1)     # Configura a linha dentro da aba

    def confirmaContrato(janela, framePrincipal):
        try:
            nomeCliente = verificaçãoNome(nomeClienteEntry.get())
            cpf = verificaçãoCPF(cpfEntry.get()) or "n/a"
            print(cpf)
            cnpj = verificaçãoCNPJ(cnpjEntry.get()) or "n/a"
            endereçoCliente = endereçoClienteEntry.get()
            endereçoObra = endereçoObraEntry.get()
            duraçaoContrato = verificaçãoDATA(duraçãoContratoEntry.get())

            quantidadeEscora = verificaçãoNUMERO(escorasEntry.get()) or 0
            quantidadeAndaime = verificaçãoNUMERO(andaimesEntry.get()) or 0
            quantidadeBetoneira = verificaçãoNUMERO(betoneirasEntry.get()) or 0
            quantidadePlataforma = verificaçãoNUMERO(plataformasEntry.get()) or 0
            quantidadeRoldana = verificaçãoNUMERO(roldanasEntry.get()) or 0
            quantidadeRegulador = verificaçãoNUMERO(reguladoresEntry.get()) or 0

            valorEscora = verificaçãoNUMERO(preçoEscoraEntry.get()) or 0
            valorAndaime = verificaçãoNUMERO(preçoAndaimeEntry.get()) or 0
            valorBetoneira = verificaçãoNUMERO(preçoBetoneiraEntry.get()) or 0
            valorPlataforma = verificaçãoNUMERO(preçoPlataformaEntry.get()) or 0
            valorRoldana = verificaçãoNUMERO(preçoRoldanaEntry.get()) or 0
            valorRegulador = verificaçãoNUMERO(preçoReguladorEntry.get()) or 0

            tamanhoEscora = verificaçãoNUMERO(tamanhoEscorasEntry.get()) or 0
            tamanhoAndaime = verificaçãoNUMERO(tamanhoAndaimesEntry.get()) or 0
            tamanhoPlataforma = verificaçãoNUMERO(tamanhoPlataformasEntry.get()) or 0

            pagamentoTotal = ((float(valorEscora) * float(quantidadeEscora)) + ((float(quantidadeAndaime) * float(valorAndaime)) + (float(quantidadeBetoneira) * float(valorBetoneira)) + (float(quantidadePlataforma) * float(valorPlataforma)) + (float(quantidadeRegulador) * float(valorRegulador)) + (float(quantidadeRoldana) * float(valorRoldana))))

            diaAtual = date.today().strftime('%d/%m/%Y')

            formaPagamento = formaPagamentoEntry.get()

            db.insert(
                {
                    'nome': nomeCliente,
                    'addresClient': endereçoCliente,
                    'addresObra': endereçoObra,
                    'cpf': cpf,
                    'cnpj': cnpj,
                    'valueEscora': valorEscora,
                    'sizeEscora': tamanhoEscora,
                    'quantity': quantidadeEscora,
                    'paymentAmount': pagamentoTotal,
                    'todayDate': diaAtual,
                    'paymentDate': duraçaoContrato,
                    'formPayment': formaPagamento,
                    'quantityAndaimes': quantidadeAndaime,
                    'valueAndaimes': valorAndaime,
                    'sizeAndaime': tamanhoAndaime,
                    'id': idCliente,
                    'quantityBetoneira': quantidadeBetoneira,
                    'valueBetoneira': valorBetoneira,
                    'quantityRoldana': quantidadeRoldana,
                    'valueRoldana': valorRoldana,
                    'quantityRegulador': quantidadeRegulador,
                    'valueRegulador': valorRegulador,
                    'quantityPlataforma': quantidadePlataforma,
                    'valuePlataforma': valorPlataforma,
                    'sizePlataforma': tamanhoPlataforma,
                    'statePayment': "Pendente"
                }
            )

            for widget in framePrincipal.winfo_children():
                if isinstance(widget, CTkEntry):
                    widget.delete(0, 'end')

            mostraMensagem("Açao bem-sucedida!", "O cliente foi cadastrado com sucesso!")
            interfaceUsuario.destroy()
            interface.deiconify()

        except TypeError:
            interfaceUsuario.destroy()
            interface.deiconify()
        except AttributeError:
            interfaceUsuario.destroy()
            interface.deiconify()

    #Tab de Cliente
    nomeClienteLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="Nome do Cliente:", text_color=corFonte, font=("roboto", 17))
    nomeClienteLabel.grid(row=0, padx=150)

    nomeClienteEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    nomeClienteEntry.grid(row=1, padx=150, pady=10, sticky="ew")

    endereçoClienteLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="Endereço do Cliente:", text_color=corFonte, font=("roboto", 17))
    endereçoClienteLabel.grid(row=2, padx=150)

    endereçoClienteEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    endereçoClienteEntry.grid(row=3, padx=150, pady=10)

    endereçoObraLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="Endereço da Obra:", text_color=corFonte, font=("roboto", 17))
    endereçoObraLabel.grid(row=4, padx=150)

    endereçoObraEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    endereçoObraEntry.grid(row=5, padx=150, pady=10)

    cpfLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="CPF do Cliente:(Opcional)", text_color=corFonte, font=("roboto", 17))
    cpfLabel.grid(row=6, padx=150)

    cpfEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    cpfEntry.grid(row=7, padx=150, pady=10)

    cnpjLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="CNPJ do Cliente:(Opcional)", text_color=corFonte, font=("roboto", 17))
    cnpjLabel.grid(row=0, column=1, padx=150)

    cnpjEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    cnpjEntry.grid(row=1, column=1, padx=150, pady=10)

    duraçãoContratoLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="Duração do Contrato:", text_color=corFonte, font=("roboto", 17))
    duraçãoContratoLabel.grid(row=2, column=1, padx=150)

    duraçãoContratoEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    duraçãoContratoEntry.grid(row=3, column=1, padx=150, pady=10)

    formaPagamentoLabel = CTkLabel(janelasCadastro.tab("Cliente"), text="Forma de Pagamento:", text_color=corFonte, font=("roboto", 17))
    formaPagamentoLabel.grid(row=4, column=1, padx=150)

    formaPagamentoEntry = CTkEntry(janelasCadastro.tab("Cliente"), width=300, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    formaPagamentoEntry.grid(row=5, column=1, padx=150, pady=10)

    #Fim Tab de Cliente

    idCliente = defineId()

    #Tab de Produtos
    if verificaçãoEstoque(escoras, 'quantity', "escoras") == 0:
        escorasLabel = CTkLabel(
        janelasCadastro.tab("Produtos"),
        text="(Nenhuma escora disponível no momento!)",
        text_color="red",
        font=("roboto", 19)
        )
        escorasLabel.grid(row=0, padx=100)

        escorasEntry = CTkEntry(
            janelasCadastro.tab("Produtos"),
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        escorasEntry.grid(row=1, padx=100, pady=10)

        preçoEscoraLabel = CTkLabel(janelasCadastro.tab("Preços"), text="(Nenhuma escora disponível no momento!)", text_color="red", font=("roboto", 19))
        preçoEscoraLabel.grid(row=0, padx=120)

        preçoEscoraEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
            )
        preçoEscoraEntry.grid(row=1, padx=120, pady=10)

    else:
        escorasLabel = CTkLabel(janelasCadastro.tab("Produtos"), text="Digite a quantidade de escoras que vão ser alugadas:\n({} escoras disponíveis)".format(mostraEstoqueDisponivel(escoras, "quantity")), text_color=corFonte, font=("roboto", 17))
        escorasLabel.grid(row=0, padx=100)

        escorasEntry = CTkEntry(janelasCadastro.tab("Produtos"), width=320, height=38, placeholder_text="Digite aqui a quantidade de escoras", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        escorasEntry.grid(row=1, padx=100, pady=10)

        preçoEscoraLabel = CTkLabel(janelasCadastro.tab("Preços"), text="Digite o preço da escora: (Unidade)", text_color=corFonte, font=("roboto", 17))
        preçoEscoraLabel.grid(row=0, padx=120)

        preçoEscoraEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        preçoEscoraEntry.grid(row=1, padx=120, pady=10)

    if verificaçãoEstoque(andaimes, 'quantityAndaimes', "andaimes") == 0:
        andaimesLabel = CTkLabel(
            janelasCadastro.tab("Produtos"), 
            text="(Nenhum andaime disponível no momento!)",
            text_color="red",
            font=("roboto", 19)
        )
        andaimesLabel.grid(row=2, padx=100)

        andaimesEntry = CTkEntry(
            janelasCadastro.tab("Produtos"), 
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        andaimesEntry.grid(row=3, padx=100, pady=10)

        preçoAndaimeLabel = CTkLabel(janelasCadastro.tab("Preços"), text="(Nenhum andaime disponível no momento!)", text_color="red", font=("roboto", 19))
        preçoAndaimeLabel.grid(row=2, padx=120)

        preçoAndaimeEntry = CTkEntry(
            janelasCadastro.tab("Preços"), 
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        preçoAndaimeEntry.grid(row=3, padx=120, pady=10)
    else:
        andaimesLabel = CTkLabel(janelasCadastro.tab("Produtos"), text="Digite a quantidade de andaimes que vão ser alugados:\n({} andaimes disponíveis)".format(mostraEstoqueDisponivel(andaimes, "quantityAndaimes")), text_color=corFonte, font=("roboto", 17))
        andaimesLabel.grid(row=2, padx=100)

        andaimesEntry = CTkEntry(janelasCadastro.tab("Produtos"), width=320, height=38, placeholder_text="Digite aqui a quantidade de andaimes", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        andaimesEntry.grid(row=3, padx=100, pady=10)

        preçoAndaimeLabel = CTkLabel(janelasCadastro.tab("Preços"), text="Digite o preço do andaime: (Unidade)", text_color=corFonte, font=("roboto", 17))
        preçoAndaimeLabel.grid(row=2, padx=120)

        preçoAndaimeEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        preçoAndaimeEntry.grid(row=3, padx=120, pady=10)
    
    if verificaçãoEstoque(betoneiras, 'quantityBetoneira', "betoneiras") == 0:
        betoneirasLabel = CTkLabel(
            janelasCadastro.tab("Produtos"), 
            text="(Nenhuma betoneira disponível no momento!)",
            text_color="red",
            font=("roboto", 19)
        )
        betoneirasLabel.grid(row=4, padx=100)

        betoneirasEntry = CTkEntry(
            janelasCadastro.tab("Produtos"), 
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        betoneirasEntry.grid(row=5, padx=100, pady=10)

        preçoBetoneiraLabel = CTkLabel(janelasCadastro.tab("Preços"), text="(Nenhuma betoneira disponível no momento!)", text_color="red", font=("roboto", 19))
        preçoBetoneiraLabel.grid(row=4, padx=120)

        preçoBetoneiraEntry = CTkEntry(
            janelasCadastro.tab("Preços"), width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        preçoBetoneiraEntry.grid(row=5, padx=120, pady=10)

    else:
        betoneirasLabel = CTkLabel(janelasCadastro.tab("Produtos"), text="Digite a quantidade de betoneiras que vão ser alugadas:\n({} betoneiras disponíveis)".format(mostraEstoqueDisponivel(betoneiras, "quantityBetoneira")), text_color=corFonte, font=("roboto", 17))
        betoneirasLabel.grid(row=4, padx=100)

        betoneirasEntry = CTkEntry(janelasCadastro.tab("Produtos"), width=320, height=38, placeholder_text="Digite aqui a quantidade de betoneiras", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        betoneirasEntry.grid(row=5, padx=100, pady=10)

        preçoBetoneiraLabel = CTkLabel(janelasCadastro.tab("Preços"), text="Digite o preço da betoneira: (Unidade)", text_color=corFonte, font=("roboto", 17))
        preçoBetoneiraLabel.grid(row=4, padx=120)

        preçoBetoneiraEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        preçoBetoneiraEntry.grid(row=5, padx=120, pady=10)

    if verificaçãoEstoque(roldanas, 'quantityRoldana', "roldanas") == 0:
        roldanasLabel = CTkLabel(
            janelasCadastro.tab("Produtos"), 
            text="(Nenhuma roldana disponível no momento!)",
            text_color="red",
            font=("roboto", 19)
        )
        roldanasLabel.grid(row=0, column=1, padx=100)

        roldanasEntry = CTkEntry(
            janelasCadastro.tab("Produtos"), 
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        roldanasEntry.grid(row=1, column=1, padx=100, pady=10)

        preçoRoldanaLabel = CTkLabel(janelasCadastro.tab("Preços"), text="(Nenhuma roldana disponível no momento!)", text_color="red", font=("roboto", 19))
        preçoRoldanaLabel.grid(row=0, column=1, padx=120)

        preçoRoldanaEntry = CTkEntry(
            janelasCadastro.tab("Preços"), width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        preçoRoldanaEntry.grid(row=1, column=1, padx=120, pady=10)

    else:
        roldanasLabel = CTkLabel(janelasCadastro.tab("Produtos"), text="Digite a quantidade de roldanas que vão ser alugadas:\n({} roldanas disponíveis)".format(mostraEstoqueDisponivel(roldanas, "quantityRoldana")), text_color=corFonte, font=("roboto", 17))
        roldanasLabel.grid(row=0, column=1, padx=100)

        roldanasEntry = CTkEntry(janelasCadastro.tab("Produtos"), width=320, height=38, placeholder_text="Digite aqui a quantidade de roldanas", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        roldanasEntry.grid(row=1, column=1, padx=100, pady=10)

        preçoRoldanaLabel = CTkLabel(janelasCadastro.tab("Preços"), text="Digite o preço da roldana: (Unidade)", text_color=corFonte, font=("roboto", 17))
        preçoRoldanaLabel.grid(row=0, column=1, padx=120)

        preçoRoldanaEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        preçoRoldanaEntry.grid(row=1, column=1, padx=120, pady=10)

    if verificaçãoEstoque(plataformas, 'quantityPlataforma', "plataformas") == 0:
        plataformasLabel = CTkLabel(
            janelasCadastro.tab("Produtos"), 
            text="(Nenhuma plataforma disponível no momento!)",
            text_color="red",
            font=("roboto", 19))
        plataformasLabel.grid(row=2, column=1, padx=100)

        plataformasEntry = CTkEntry(
            janelasCadastro.tab("Produtos"), 
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled")
        plataformasEntry.grid(row=3, column=1, padx=100, pady=10)

        preçoPlataformaLabel = CTkLabel(janelasCadastro.tab("Preços"), text="(Nenhuma plataforma disponível no momento!)", text_color="red", font=("roboto", 19))
        preçoPlataformaLabel.grid(row=2, column=1, padx=120)

        preçoPlataformaEntry = CTkEntry(
            janelasCadastro.tab("Preços"), width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        preçoPlataformaEntry.grid(row=3, column=1, padx=120, pady=10)

    else:
        plataformasLabel = CTkLabel(janelasCadastro.tab("Produtos"), text="Digite a quantidade de plataformas que vão ser alugadas:\n({} plataformas disponíveis)".format(mostraEstoqueDisponivel(plataformas, "quantityPlataforma")), text_color=corFonte, font=("roboto", 17))
        plataformasLabel.grid(row=2, column=1, padx=100)

        plataformasEntry = CTkEntry(janelasCadastro.tab("Produtos"), width=320, height=38, placeholder_text="Digite aqui a quantidade de plataformas", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        plataformasEntry.grid(row=3, column=1, padx=100, pady=10)

        preçoPlataformaLabel = CTkLabel(janelasCadastro.tab("Preços"), text="Digite o preço da plataforma: (Unidade)", text_color=corFonte, font=("roboto", 17))
        preçoPlataformaLabel.grid(row=2, column=1, padx=120)

        preçoPlataformaEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        preçoPlataformaEntry.grid(row=3, column=1, padx=120, pady=10)

    if verificaçãoEstoque(reguladores, 'quantityRegulador', "reguladores") == 0:
        reguladoresLabel = CTkLabel(
            janelasCadastro.tab("Produtos"), 
            text="(Nenhum regulador disponível no momento!)",
            text_color="red",
            font=("roboto", 19))
        reguladoresLabel.grid(row=4, column=1, padx=100)

        reguladoresEntry = CTkEntry(
            janelasCadastro.tab("Produtos"), 
            width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled")
        reguladoresEntry.grid(row=5, column=1, padx=100, pady=10)

        preçoPlataformaLabel = CTkLabel(janelasCadastro.tab("Preços"), text="(Nenhum regulador disponível no momento!)", text_color="red", font=("roboto", 19))
        preçoPlataformaLabel.grid(row=4, column=1, padx=120)

        preçoPlataformaEntry = CTkEntry(
            janelasCadastro.tab("Preços"), width=320,
            height=38,
            placeholder_text="Não disponível",
            corner_radius=10,
            fg_color=corFundoFrame,
            text_color="gray",
            placeholder_text_color="#DAD8DF",
            font=("roboto", 17),
            state="disabled"
        )
        preçoPlataformaEntry.grid(row=5, column=1, padx=120, pady=10)

    else:
        reguladoresLabel = CTkLabel(janelasCadastro.tab("Produtos"), text="Digite a quantidade de reguladores que vão ser alugados:\n({} reguladores disponíveis)".format(mostraEstoqueDisponivel(reguladores, "quantityRegulador")), text_color=corFonte, font=("roboto", 17))
        reguladoresLabel.grid(row=4, column=1, padx=100)

        reguladoresEntry = CTkEntry(janelasCadastro.tab("Produtos"), width=320, height=38, placeholder_text="Digite aqui a quantidade de reguladores", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        reguladoresEntry.grid(row=5, column=1, padx=100, pady=10)

        preçoReguladorLabel = CTkLabel(janelasCadastro.tab("Preços"), text="Digite o preço do regulador: (Unidade)", text_color=corFonte, font=("roboto", 17))
        preçoReguladorLabel.grid(row=4, column=1, padx=120)

        preçoReguladorEntry = CTkEntry(janelasCadastro.tab("Preços"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
        preçoReguladorEntry.grid(row=5, column=1, padx=120, pady=10)

    #Fim Tab de Produtos

    #Inicio Tab de Tamanhos

    tamanhoPlataformasLabel = CTkLabel(janelasCadastro.tab("Tamanhos"), text="Digite o tamanho das plataformas que vão ser alugadas:", text_color=corFonte, font=("roboto", 17))
    tamanhoPlataformasLabel.grid(row=0, padx=100)

    tamanhoPlataformasEntry = CTkEntry(janelasCadastro.tab("Tamanhos"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    tamanhoPlataformasEntry.grid(row=1, padx=100, pady=10)

    tamanhoEscorasLabel = CTkLabel(janelasCadastro.tab("Tamanhos"), text="Digite o tamanho das escoras que vão ser alugadas:", text_color=corFonte, font=("roboto", 17))
    tamanhoEscorasLabel.grid(row=2, padx=100)

    tamanhoEscorasEntry = CTkEntry(janelasCadastro.tab("Tamanhos"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    tamanhoEscorasEntry.grid(row=3, padx=100, pady=10)

    tamanhoAndaimesLabel = CTkLabel(janelasCadastro.tab("Tamanhos"), text="Digite o tamanho dos andaimes que vão ser alugadas:", text_color=corFonte, font=("roboto", 17))
    tamanhoAndaimesLabel.grid(row=4, padx=100)

    tamanhoAndaimesEntry = CTkEntry(janelasCadastro.tab("Tamanhos"), width=320, height=38, placeholder_text="Digite aqui...", corner_radius=10, fg_color=corFundoFrame, text_color=corFonte, placeholder_text_color="#DAD8DF", font=("roboto", 17))
    tamanhoAndaimesEntry.grid(row=5, padx=100, pady=10)
    
    #Fim Tab de Tamanhos

