package com.erudia.demo.resource;

import java.util.HashMap;

import javax.annotation.Generated;

import com.FiltroAndReco.*;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;


@RestController
@RequestMapping("/requisitar")
public class RequisicaoResource {

    private IndexMannager mIndexBuscar = new IndexMannager(7000, 101);
    private IndexMannager mIndexBuscarMaisPopulares = new IndexMannager(7103, 101);
    private IndexMannager mIndexRecomendacao = new IndexMannager(7208, 101);

  //  String resp = JythonComunication.SendToPython(mIndex, fala);
                                                                        //Preço e Qtd de Vizualização
    @GetMapping("/busca/{pesquisa}/{categoria}/{idCliente}/{valormin}/{valormax}/{ordenacao}")
    public HashMap<String, Object> buscar(@PathVariable String pesquisa, @PathVariable String categoria, @PathVariable String idCliente , @PathVariable String valormin, @PathVariable String valormax, @PathVariable String ordenacao ) {
        //TODO Parsear Categoria 
        //String entradaDaBusca = "camisa,masculina|moderna|nike,0,2,DESC"
        String entradaDaBusca = pesquisa  + "," + categoria + "," + idCliente + ","  +  valormax  + "," + valormin  + "," + ordenacao;
        String resp = JythonComunication.SendToPython(mIndexBuscar, entradaDaBusca);
        HashMap<String, Object> map = new HashMap<>();
        return null;
    }

    @GetMapping("/maispop")
    public HashMap<String, Object> buscarMaisPopulares() {
        String respostaDosPopulares = JythonComunication.SendToPython(mIndexBuscarMaisPopulares, "");
        HashMap<String, Object> map = new HashMap<>();
        return null;
    }

    @GetMapping("/bucarrelacionado/{idCliente}/{idProduto}")
    public HashMap<String, Object> recomendacaoDadoProduto(@PathVariable int idCliente, @PathVariable int idProduto) {
        String recomendacaoParaCliente = JythonComunication.SendToPython(mIndexRecomendacao, "" + idCliente + "," + idProduto);
        return null;
    }

    private HashMap<String,Object> montar(String p) {
        return null;
    }
    

    // @GetMapping("/busca/{pesquisa}/{categoria}/{idCliente}/{valormin}/{valormax}/{ordenacao}")
    // public HashMap<String, Object> buscar(@PathVariable String pesquisa, @PathVariable String categoria, @PathVariable String idCliente , @PathVariable String valormin, @PathVariable String valormax, @PathVariable String ordenacao ) {
    //     //TODO Parsear Categoria 
    //     //String entradaDaBusca = "camisa,masculina|moderna|nike,0,2,DESC"
    //     String entradaDaBusca = pesquisa  + "," + categoria + "," + idCliente + ","  +  valormax  + "," + valormin  + "," + ordenacao;
    //     String resp = JythonComunication.SendToPython(mIndexBuscar, entradaDaBusca);
    //     HashMap<String, Object> map = new HashMap<>();
    //     return null;
    // }

    // @GetMapping("/maispop")
    // public HashMap<String, Object> buscarMaisPopulares() {
    //     String respostaDosPopulares = JythonComunication.SendToPython(mIndexBuscarMaisPopulares, "");
    //     HashMap<String, Object> map = new HashMap<>();
    //     return null;
    // }

    // @GetMapping("/bucarrelacionado/{idCliente}/{idProduto}")
    // public HashMap<String, Object> recomendacaoDadoProduto(@PathVariable int idCliente, @PathVariable int idProduto) {
    //     String recomendacaoParaCliente = JythonComunication.SendToPython(mIndexRecomendacao, "" + idCliente + "," + idProduto);
    //     return null;
    // }


}