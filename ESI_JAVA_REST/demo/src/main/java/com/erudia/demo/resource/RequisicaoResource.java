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

    @GetMapping("/busca/{pesquisa}/{categoria}/{valormin}/{valormax}/{ordenacao}")
    public HashMap<String, Object> buscar(@PathVariable String pesquisa, @PathVariable String categoria, @PathVariable String valormin, @PathVariable String valormax, @PathVariable String ordenacao ) {
        //TODO Parsear Categoria 
        //String entradaDaBusca = "camisa,masculina|moderna|nike,0,2,DESC"
        String entradaDaBusca = pesquisa  + "," + categoria + "," + valormin + "," + valormax + "," + ordenacao;
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

    @GetMapping("/cliente/{idCliente}")
    public HashMap<String, Object> recomendacao(@PathVariable int idCliente) {
        String recomendacaoParaCliente = JythonComunication.SendToPython(mIndexRecomendacao, "" + idCliente);
        return null;
    }
    



}