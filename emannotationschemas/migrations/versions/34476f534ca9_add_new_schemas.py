"""Add new schemas

Revision ID: 34476f534ca9
Revises: bc42c1e4cc1a
Create Date: 2022-06-22 15:55:42.042381

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision = '34476f534ca9'
down_revision = 'bc42c1e4cc1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bound_double_tag',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('superceded_id', sa.BigInteger(), nullable=True),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('pt_position', Geometry(geometry_type='POINTZ', dimension=3, use_N_D_index=True, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('tag', sa.String(), nullable=True),
    sa.Column('tag2', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bound_double_tag_created'), 'bound_double_tag', ['created'], unique=False)
    op.create_index(op.f('ix_bound_double_tag_deleted'), 'bound_double_tag', ['deleted'], unique=False)
    op.create_table('bound_double_tag_user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('superceded_id', sa.BigInteger(), nullable=True),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('pt_position', Geometry(geometry_type='POINTZ', dimension=3, use_N_D_index=True, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('tag', sa.String(), nullable=True),
    sa.Column('tag2', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bound_double_tag_user_created'), 'bound_double_tag_user', ['created'], unique=False)
    op.create_index(op.f('ix_bound_double_tag_user_deleted'), 'bound_double_tag_user', ['deleted'], unique=False)
    op.create_table('fly_cell_type',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('superceded_id', sa.BigInteger(), nullable=True),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('pt_position', Geometry(geometry_type='POINTZ', dimension=3, use_N_D_index=True, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('cell_type', sa.String(), nullable=True),
    sa.Column('hemisphere', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fly_cell_type_created'), 'fly_cell_type', ['created'], unique=False)
    op.create_index(op.f('ix_fly_cell_type_deleted'), 'fly_cell_type', ['deleted'], unique=False)
    op.create_table('fly_cell_type_ext',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('superceded_id', sa.BigInteger(), nullable=True),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('pt_position', Geometry(geometry_type='POINTZ', dimension=3, use_N_D_index=True, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('cell_type', sa.String(), nullable=True),
    sa.Column('hemisphere', sa.String(), nullable=True),
    sa.Column('driver_line', sa.String(), nullable=True),
    sa.Column('synonym', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fly_cell_type_ext_created'), 'fly_cell_type_ext', ['created'], unique=False)
    op.create_index(op.f('ix_fly_cell_type_ext_deleted'), 'fly_cell_type_ext', ['deleted'], unique=False)
    op.create_table('bound_double_tag__tests_pcg',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('pt_supervoxel_id', sa.BigInteger(), nullable=True),
    sa.Column('pt_root_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['bound_double_tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bound_double_tag__tests_pcg_pt_root_id'), 'bound_double_tag__tests_pcg', ['pt_root_id'], unique=False)
    op.create_table('bound_double_tag_user__tests_pcg',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('pt_supervoxel_id', sa.BigInteger(), nullable=True),
    sa.Column('pt_root_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['bound_double_tag_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bound_double_tag_user__tests_pcg_pt_root_id'), 'bound_double_tag_user__tests_pcg', ['pt_root_id'], unique=False)
    op.create_table('fly_cell_type__tests_pcg',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('pt_supervoxel_id', sa.BigInteger(), nullable=True),
    sa.Column('pt_root_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['fly_cell_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fly_cell_type__tests_pcg_pt_root_id'), 'fly_cell_type__tests_pcg', ['pt_root_id'], unique=False)
    op.create_table('fly_cell_type_ext__tests_pcg',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('pt_supervoxel_id', sa.BigInteger(), nullable=True),
    sa.Column('pt_root_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['fly_cell_type_ext.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fly_cell_type_ext__tests_pcg_pt_root_id'), 'fly_cell_type_ext__tests_pcg', ['pt_root_id'], unique=False)
    op.create_table('reference_simple_group',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('deleted', sa.DateTime(), nullable=True),
    sa.Column('superceded_id', sa.BigInteger(), nullable=True),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('target_id', sa.BigInteger(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['target_id'], ['reference_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reference_simple_group_created'), 'reference_simple_group', ['created'], unique=False)
    op.create_index(op.f('ix_reference_simple_group_deleted'), 'reference_simple_group', ['deleted'], unique=False)
    op.create_index(op.f('ix_reference_simple_group_target_id'), 'reference_simple_group', ['target_id'], unique=False)
    op.create_table('reference_simple_group__tests_pcg',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['reference_simple_group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reference_simple_group__tests_pcg')
    op.drop_index(op.f('ix_reference_simple_group_target_id'), table_name='reference_simple_group')
    op.drop_index(op.f('ix_reference_simple_group_deleted'), table_name='reference_simple_group')
    op.drop_index(op.f('ix_reference_simple_group_created'), table_name='reference_simple_group')
    op.drop_table('reference_simple_group')
    op.drop_index(op.f('ix_fly_cell_type_ext__tests_pcg_pt_root_id'), table_name='fly_cell_type_ext__tests_pcg')
    op.drop_table('fly_cell_type_ext__tests_pcg')
    op.drop_index(op.f('ix_fly_cell_type__tests_pcg_pt_root_id'), table_name='fly_cell_type__tests_pcg')
    op.drop_table('fly_cell_type__tests_pcg')
    op.drop_index(op.f('ix_bound_double_tag_user__tests_pcg_pt_root_id'), table_name='bound_double_tag_user__tests_pcg')
    op.drop_table('bound_double_tag_user__tests_pcg')
    op.drop_index(op.f('ix_bound_double_tag__tests_pcg_pt_root_id'), table_name='bound_double_tag__tests_pcg')
    op.drop_table('bound_double_tag__tests_pcg')
    op.drop_index(op.f('ix_fly_cell_type_ext_deleted'), table_name='fly_cell_type_ext')
    op.drop_index(op.f('ix_fly_cell_type_ext_created'), table_name='fly_cell_type_ext')
    op.drop_table('fly_cell_type_ext')
    op.drop_index(op.f('ix_fly_cell_type_deleted'), table_name='fly_cell_type')
    op.drop_index(op.f('ix_fly_cell_type_created'), table_name='fly_cell_type')
    op.drop_table('fly_cell_type')
    op.drop_index(op.f('ix_bound_double_tag_user_deleted'), table_name='bound_double_tag_user')
    op.drop_index(op.f('ix_bound_double_tag_user_created'), table_name='bound_double_tag_user')
    op.drop_table('bound_double_tag_user')
    op.drop_index(op.f('ix_bound_double_tag_deleted'), table_name='bound_double_tag')
    op.drop_index(op.f('ix_bound_double_tag_created'), table_name='bound_double_tag')
    op.drop_table('bound_double_tag')
    # ### end Alembic commands ###
