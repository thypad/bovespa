class Company:
    def __init__(self, cvm_code=None, social_name=None,
                cnpj=None, sector=None):
        self.cvm_code = cvm_code
        self.social_name = social_name
        self.cnpj = cnpj

        self.sector = None
        self.subsector = None
        self.segment = None
