inflation_report_email: str = (
    """
    <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Boletim de Inflação - PUCPR</title>
                <style>
                    /* Cores da PUCPR */
                    body {
                        background-color: #201c26; /* Cor institucional - Burgundy */
                        color: #fff; /* Texto em branco */
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                    }
                    .container {
                        width: 80%;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    h1 {
                        font-size: 24px;
                        color: #ffcc29; /* Cor auxiliar - Amarelo */
                    }
                    p {
                        font-size: 16px;
                    }
                    .pucpr-logo {
                        max-width: 100px; /* Tamanho da logo */
                        display: block;
                        margin: 20px auto; /* Centralizar a logo */
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <img src="https://sites.pucpr.br/empresas/wp-content/uploads/sites/44/2022/08/logo-pucpr-icon-1.png" alt="Logo PUCPR" class="pucpr-logo">
                    <h1>Boletim de Inflação - PUCPR</h1>
                    <p>__MESSAGE_</p>
                </div>
            </body>
        </html>
    """
)
