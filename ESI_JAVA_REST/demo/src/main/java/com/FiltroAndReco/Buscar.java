package com.FiltroAndReco;

import java.util.ArrayList;
import java.util.HashMap;

public class Buscar{

    public Buscar(){

    }
    
    String[] produtos = new String[10];
    
    public String relacionados(String buscado) {
        produtos[0] = "Duas COisas";
        if(produtos[0].equals(buscado)){
            return produtos[0];
        }
        else return "Nao Achei Duas vezes!";

    }

    public String buscarProdutosTeste(String produtoPesquisado){
        produtos[0] = "camiseta";
        produtos[1] = "meia";
        produtos[2] = "blusa";
        produtos[3] = "calca";
        produtos[4] = "bone";
        produtos[5] = "cueca";

        for(int i = 0; i<6; i++){

            if(produtos[i].equals(produtoPesquisado)){
                return produtos[i];
            }            
        }

        return "Produto Nao Encontrado";
    }

    public HashMap<String, Object> buscarProdutos(String produtoPesquisado) {

        return null;
    }

    public HashMap<String, Object> buscarMaisPopulares(int quantidadeRequisitada) {
        return null;
    }

    public HashMap<String, Object> buscarPorHistoricoCliente(int idCliente) {

        return null;
    }


}