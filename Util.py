# Databricks notebook source
# MAGIC %md
# MAGIC # Comando para mover uma tabela de lugar

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE houseprices.default.bronze_test RENAME TO houseprices.bronze.bronze_test;

# COMMAND ----------

# MAGIC %md
# MAGIC # Comando para deletar um schema

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP SCHEMA workspace.gold CASCADE;
