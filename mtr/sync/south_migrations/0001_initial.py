# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Settings'
        db.create_table(u'mtr_sync_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('start_row', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('end_row', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('processor', self.gf('django.db.models.fields.CharField')(default='XlsxProcessor', max_length=255)),
            ('worksheet', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('include_header', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('buffer_file', self.gf('django.db.models.fields.files.FileField')(db_index=True, max_length=100, blank=True)),
            ('dataset', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('data_action', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('filter_dataset', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('filter_querystring', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('hide_translation_fields', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_fields', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('populate_from_file', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('include_related', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('edit_attributes', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mtr_sync', ['Settings'])

        # Adding model 'Sequence'
        db.create_table(u'mtr_sync_sequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('buffer_file', self.gf('django.db.models.fields.files.FileField')(db_index=True, max_length=100, blank=True)),
        ))
        db.send_create_signal('mtr_sync', ['Sequence'])

        # Adding M2M table for field settings on 'Sequence'
        m2m_table_name = db.shorten_name(u'mtr_sync_sequence_settings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sequence', models.ForeignKey(orm['mtr_sync.sequence'], null=False)),
            ('settings', models.ForeignKey(orm['mtr_sync.settings'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sequence_id', 'settings_id'])

        # Adding model 'ReplacerCategory'
        db.create_table(u'mtr_sync_replacercategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('mtr_sync', ['ReplacerCategory'])

        # Adding model 'Replacer'
        db.create_table(u'mtr_sync_replacer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.TextField')(max_length=100000)),
            ('change_to', self.gf('django.db.models.fields.TextField')(max_length=100000)),
            ('regex', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='replacers', null=True, to=orm['mtr_sync.ReplacerCategory'])),
        ))
        db.send_create_signal('mtr_sync', ['Replacer'])

        # Adding model 'Field'
        db.create_table(u'mtr_sync_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('skip', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('update', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('find', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('set_filter', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('set_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('find_filter', self.gf('django.db.models.fields.CharField')(default='exact', max_length=255, blank=True)),
            ('find_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('replacer_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fields', null=True, to=orm['mtr_sync.ReplacerCategory'])),
            ('converters', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('settings', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['mtr_sync.Settings'])),
        ))
        db.send_create_signal('mtr_sync', ['Field'])

        # Adding model 'Context'
        db.create_table(u'mtr_sync_context', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('settings', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contexts', null=True, to=orm['mtr_sync.Settings'])),
        ))
        db.send_create_signal('mtr_sync', ['Context'])

        # Adding model 'Report'
        db.create_table(u'mtr_sync_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
            ('buffer_file', self.gf('django.db.models.fields.files.FileField')(db_index=True, max_length=100, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('started_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('completed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('settings', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='reports', null=True, to=orm['mtr_sync.Settings'])),
        ))
        db.send_create_signal('mtr_sync', ['Report'])

        # Adding model 'Message'
        db.create_table(u'mtr_sync_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, null=True, blank=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['mtr_sync.Report'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('step', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('input_position', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('input_value', self.gf('django.db.models.fields.TextField')(max_length=60000, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('mtr_sync', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table(u'mtr_sync_settings')

        # Deleting model 'Sequence'
        db.delete_table(u'mtr_sync_sequence')

        # Removing M2M table for field settings on 'Sequence'
        db.delete_table(db.shorten_name(u'mtr_sync_sequence_settings'))

        # Deleting model 'ReplacerCategory'
        db.delete_table(u'mtr_sync_replacercategory')

        # Deleting model 'Replacer'
        db.delete_table(u'mtr_sync_replacer')

        # Deleting model 'Field'
        db.delete_table(u'mtr_sync_field')

        # Deleting model 'Context'
        db.delete_table(u'mtr_sync_context')

        # Deleting model 'Report'
        db.delete_table(u'mtr_sync_report')

        # Deleting model 'Message'
        db.delete_table(u'mtr_sync_message')


    models = {
        'mtr_sync.context': {
            'Meta': {'object_name': 'Context'},
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'settings': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contexts'", 'null': 'True', 'to': "orm['mtr_sync.Settings']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'mtr_sync.field': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Field'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'converters': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'find': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'find_filter': ('django.db.models.fields.CharField', [], {'default': "'exact'", 'max_length': '255', 'blank': 'True'}),
            'find_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'replacer_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fields'", 'null': 'True', 'to': "orm['mtr_sync.ReplacerCategory']"}),
            'set_filter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'set_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'settings': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['mtr_sync.Settings']"}),
            'skip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'update': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'mtr_sync.message': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_position': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'input_value': ('django.db.models.fields.TextField', [], {'max_length': '60000', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': "orm['mtr_sync.Report']"}),
            'step': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mtr_sync.replacer': {
            'Meta': {'object_name': 'Replacer'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'replacers'", 'null': 'True', 'to': "orm['mtr_sync.ReplacerCategory']"}),
            'change_to': ('django.db.models.fields.TextField', [], {'max_length': '100000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regex': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'value': ('django.db.models.fields.TextField', [], {'max_length': '100000'})
        },
        'mtr_sync.replacercategory': {
            'Meta': {'object_name': 'ReplacerCategory'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mtr_sync.report': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Report'},
            'action': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'buffer_file': ('django.db.models.fields.files.FileField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'completed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'settings': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports'", 'null': 'True', 'to': "orm['mtr_sync.Settings']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'mtr_sync.sequence': {
            'Meta': {'object_name': 'Sequence'},
            'buffer_file': ('django.db.models.fields.files.FileField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'settings': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sequences'", 'symmetrical': 'False', 'to': "orm['mtr_sync.Settings']"})
        },
        'mtr_sync.settings': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Settings'},
            'action': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'buffer_file': ('django.db.models.fields.files.FileField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'create_fields': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_action': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dataset': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'edit_attributes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_row': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'filter_dataset': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'filter_querystring': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hide_translation_fields': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'include_related': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'populate_from_file': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'processor': ('django.db.models.fields.CharField', [], {'default': "'XlsxProcessor'", 'max_length': '255'}),
            'start_row': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'worksheet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['mtr_sync']